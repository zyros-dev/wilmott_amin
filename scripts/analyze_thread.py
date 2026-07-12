#!/usr/bin/env python3
"""
Analyze the Wilmott thread: sentiment, word usage, posting frequency over time.
Outputs a PDF report with visualizations.
"""

import re
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

# Try to import optional NLP libraries
try:
    from textblob import TextBlob
    HAS_TEXTBLOB = True
except ImportError:
    HAS_TEXTBLOB = False
    print("Note: pip install textblob for sentiment analysis")

RAW_DIR = Path("./archive/raw")
OUTPUT_PDF = Path("./reports/wilmott_analysis.pdf")
SCRAPE_DATE = datetime(2026, 7, 12)


def parse_forum_timestamp(timestamp_str):
    """Parse absolute and scrape-relative phpBB timestamps."""
    if timestamp_str.startswith("Today,"):
        time_part = timestamp_str.removeprefix("Today,").strip()
        parsed_time = datetime.strptime(time_part, "%I:%M %p")
        return SCRAPE_DATE.replace(hour=parsed_time.hour, minute=parsed_time.minute)
    if timestamp_str.startswith("Yesterday,"):
        time_part = timestamp_str.removeprefix("Yesterday,").strip()
        parsed_time = datetime.strptime(time_part, "%I:%M %p")
        yesterday = SCRAPE_DATE - timedelta(days=1)
        return yesterday.replace(hour=parsed_time.hour, minute=parsed_time.minute)

    ts = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', timestamp_str)
    for format_string in ('%B %d, %Y, %I:%M %p', '%B %d, %Y, %I:%M%p'):
        try:
            return datetime.strptime(ts, format_string)
        except ValueError:
            continue
    return None

def parse_posts():
    """Extract posts with metadata from raw HTML files."""
    posts = []

    html_files = sorted(RAW_DIR.glob("page_start_*.html"))

    # Pattern to extract post number, then find associated metadata
    post_pattern = re.compile(
        r'<a class="icon_post_target"[^>]*>#(\d+)</a>.*?'
        r'<span class="timestamp">([^<]+)</span>.*?'
        r'<div class="content">(.*?)</div>\s*(?=<div class="back2top|<div class="post|<div class="notice|$)',
        re.DOTALL
    )

    # Separate pattern for author (appears before the post)
    author_pattern = re.compile(
        r'<a[^>]*class="username"[^>]*>([^<]+)</a>.*?'
        r'<a class="icon_post_target"[^>]*>#(\d+)</a>',
        re.DOTALL
    )

    seen = set()
    for html_file in html_files:
        content = html_file.read_text(encoding='utf-8')

        # Build author map from this page
        author_map = {}
        for match in author_pattern.finditer(content):
            author = match.group(1).strip()
            post_num = int(match.group(2))
            author_map[post_num] = author

        for match in post_pattern.finditer(content):
            post_num = int(match.group(1))
            if post_num in seen:
                continue
            seen.add(post_num)

            timestamp_str = match.group(2).strip()
            post_content = match.group(3)

            timestamp = parse_forum_timestamp(timestamp_str)

            # Clean content: remove HTML tags, decode entities
            text = re.sub(r'<[^>]+>', ' ', post_content)
            text = re.sub(r'&[a-z]+;', ' ', text)
            text = re.sub(r'\s+', ' ', text).strip()

            author = author_map.get(post_num, 'Unknown')

            posts.append({
                'num': post_num,
                'author': author,
                'timestamp': timestamp,
                'text': text,
                'length': len(text)
            })

    posts.sort(key=lambda p: p['num'])
    return posts


def analyze_posting_frequency(posts):
    """Analyze posts per week/month over time."""
    by_week = defaultdict(int)
    by_month = defaultdict(int)
    by_author_week = defaultdict(lambda: defaultdict(int))

    for post in posts:
        if post['timestamp']:
            week = post['timestamp'].strftime('%Y-W%W')
            month = post['timestamp'].strftime('%Y-%m')
            by_week[week] += 1
            by_month[month] += 1
            by_author_week[post['author']][week] += 1

    return dict(by_week), dict(by_month), dict(by_author_week)


def analyze_authors(posts):
    """Analyze post counts and activity by author."""
    author_posts = defaultdict(list)
    for post in posts:
        author_posts[post['author']].append(post)

    stats = {}
    for author, author_post_list in author_posts.items():
        timestamps = [p['timestamp'] for p in author_post_list if p['timestamp']]
        stats[author] = {
            'count': len(author_post_list),
            'avg_length': np.mean([p['length'] for p in author_post_list]),
            'first_post': min(timestamps) if timestamps else None,
            'last_post': max(timestamps) if timestamps else None,
        }

    return stats


def analyze_sentiment(posts):
    """Analyze sentiment over time (requires textblob)."""
    if not HAS_TEXTBLOB:
        return None

    sentiments = []
    for post in posts:
        if post['text'] and post['timestamp']:
            blob = TextBlob(post['text'][:5000])  # Limit text length
            sentiments.append({
                'num': post['num'],
                'timestamp': post['timestamp'],
                'author': post['author'],
                'polarity': blob.sentiment.polarity,  # -1 to 1
                'subjectivity': blob.sentiment.subjectivity  # 0 to 1
            })

    return sentiments


def analyze_vocabulary(posts, author=None):
    """Analyze word frequency and vocabulary changes."""
    word_counts = Counter()
    bigram_counts = Counter()

    # Technical terms to track
    tech_terms = ['hermite', 'sde', 'volatility', 'drift', 'monte carlo', 'simulation',
                  'brownian', 'stochastic', 'integral', 'differential', 'convergence',
                  'euler', 'milstein', 'density', 'distribution', 'gaussian', 'normal']
    tech_usage = defaultdict(lambda: defaultdict(int))

    for post in posts:
        if author and post['author'] != author:
            continue

        words = re.findall(r'\b[a-z]{3,}\b', post['text'].lower())
        word_counts.update(words)

        # Bigrams
        for i in range(len(words) - 1):
            bigram_counts[(words[i], words[i+1])] += 1

        # Track technical term usage over time
        if post['timestamp']:
            month = post['timestamp'].strftime('%Y-%m')
            text_lower = post['text'].lower()
            for term in tech_terms:
                if term in text_lower:
                    tech_usage[term][month] += 1

    return word_counts, bigram_counts, dict(tech_usage)


def create_pdf_report(posts, output_path):
    """Generate PDF report with visualizations."""

    print("Analyzing posting frequency...")
    by_week, by_month, by_author_week = analyze_posting_frequency(posts)

    print("Analyzing authors...")
    author_stats = analyze_authors(posts)

    print("Analyzing vocabulary...")
    word_counts, bigram_counts, tech_usage = analyze_vocabulary(posts)

    # Find main author (Amin)
    main_author = max(author_stats.keys(), key=lambda a: author_stats[a]['count'])
    print(f"Main author: {main_author} ({author_stats[main_author]['count']} posts)")

    main_author_words, _, main_tech_usage = analyze_vocabulary(posts, author=main_author)

    print("Analyzing sentiment...")
    sentiments = analyze_sentiment(posts)

    # Create PDF
    with PdfPages(output_path) as pdf:

        # Page 1: Overview stats
        fig, axes = plt.subplots(2, 2, figsize=(11, 8.5))
        fig.suptitle('Wilmott Thread Analysis: Breakthrough in SDEs', fontsize=14, fontweight='bold')

        # Top authors
        ax = axes[0, 0]
        top_authors = sorted(author_stats.items(), key=lambda x: -x[1]['count'])[:15]
        authors = [a[0][:15] for a in top_authors]
        counts = [a[1]['count'] for a in top_authors]
        ax.barh(authors[::-1], counts[::-1])
        ax.set_xlabel('Number of Posts')
        ax.set_title('Top 15 Contributors')

        # Posts per month
        ax = axes[0, 1]
        months = sorted(by_month.keys())
        month_counts = [by_month[m] for m in months]
        ax.plot(range(len(months)), month_counts, 'b-', linewidth=1)
        ax.fill_between(range(len(months)), month_counts, alpha=0.3)
        ax.set_xticks(range(0, len(months), max(1, len(months)//8)))
        ax.set_xticklabels([months[i] for i in range(0, len(months), max(1, len(months)//8))], rotation=45, ha='right')
        ax.set_ylabel('Posts')
        ax.set_title('Posts per Month')

        # Post length distribution
        ax = axes[1, 0]
        lengths = [p['length'] for p in posts]
        ax.hist(lengths, bins=50, edgecolor='black', alpha=0.7)
        ax.set_xlabel('Post Length (characters)')
        ax.set_ylabel('Frequency')
        ax.set_title('Post Length Distribution')
        ax.axvline(np.median(lengths), color='r', linestyle='--', label=f'Median: {int(np.median(lengths))}')
        ax.legend()

        # Top words (excluding common)
        ax = axes[1, 1]
        stop_words = {'the', 'and', 'that', 'this', 'with', 'for', 'are', 'but', 'not', 'you',
                      'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'has', 'have',
                      'been', 'would', 'will', 'your', 'from', 'they', 'which', 'their', 'there',
                      'what', 'about', 'when', 'make', 'like', 'time', 'just', 'know', 'take',
                      'into', 'than', 'them', 'very', 'also', 'some', 'could', 'these', 'then'}
        top_words = [(w, c) for w, c in word_counts.most_common(100) if w not in stop_words][:20]
        words = [w[0] for w in top_words]
        wcounts = [w[1] for w in top_words]
        ax.barh(words[::-1], wcounts[::-1], color='green', alpha=0.7)
        ax.set_xlabel('Frequency')
        ax.set_title('Top 20 Words (excl. common)')

        plt.tight_layout()
        pdf.savefig(fig)
        plt.close()

        # Page 2: Main author analysis
        fig, axes = plt.subplots(2, 2, figsize=(11, 8.5))
        fig.suptitle(f'Analysis of Main Author: {main_author}', fontsize=14, fontweight='bold')

        # Author's posts over time
        ax = axes[0, 0]
        author_months = sorted(by_author_week[main_author].keys())
        # Aggregate weeks to months for cleaner view
        author_by_month = defaultdict(int)
        for post in posts:
            if post['author'] == main_author and post['timestamp']:
                month = post['timestamp'].strftime('%Y-%m')
                author_by_month[month] += 1
        months_sorted = sorted(author_by_month.keys())
        ax.bar(range(len(months_sorted)), [author_by_month[m] for m in months_sorted], alpha=0.7)
        ax.set_xticks(range(0, len(months_sorted), max(1, len(months_sorted)//6)))
        ax.set_xticklabels([months_sorted[i] for i in range(0, len(months_sorted), max(1, len(months_sorted)//6))], rotation=45, ha='right')
        ax.set_ylabel('Posts')
        ax.set_title(f'{main_author} Posts per Month')

        # Author's top words
        ax = axes[0, 1]
        author_top = [(w, c) for w, c in main_author_words.most_common(100) if w not in stop_words][:15]
        ax.barh([w[0] for w in author_top][::-1], [w[1] for w in author_top][::-1], color='purple', alpha=0.7)
        ax.set_xlabel('Frequency')
        ax.set_title(f'{main_author} Top Words')

        # Author's post lengths over time
        ax = axes[1, 0]
        author_posts = [(p['num'], p['length']) for p in posts if p['author'] == main_author]
        ax.scatter([p[0] for p in author_posts], [p[1] for p in author_posts], alpha=0.3, s=10)
        # Rolling average
        window = 20
        if len(author_posts) > window:
            rolling = np.convolve([p[1] for p in author_posts], np.ones(window)/window, mode='valid')
            ax.plot([p[0] for p in author_posts][window-1:], rolling, 'r-', linewidth=2, label=f'{window}-post avg')
            ax.legend()
        ax.set_xlabel('Post Number')
        ax.set_ylabel('Length (chars)')
        ax.set_title(f'{main_author} Post Length Over Time')

        # Technical terms usage over time
        ax = axes[1, 1]
        key_terms = ['hermite', 'simulation', 'density', 'convergence']
        for term in key_terms:
            if term in main_tech_usage:
                months = sorted(main_tech_usage[term].keys())
                values = [main_tech_usage[term].get(m, 0) for m in months]
                if sum(values) > 5:  # Only plot if term used enough
                    ax.plot(range(len(months)), values, label=term, linewidth=1.5)
        ax.set_xlabel('Month')
        ax.set_ylabel('Mentions')
        ax.set_title('Technical Term Usage Over Time')
        ax.legend(fontsize=8)

        plt.tight_layout()
        pdf.savefig(fig)
        plt.close()

        # Page 3: Sentiment analysis (if available)
        if sentiments:
            fig, axes = plt.subplots(2, 2, figsize=(11, 8.5))
            fig.suptitle('Sentiment Analysis', fontsize=14, fontweight='bold')

            # Overall sentiment over time (rolling average)
            ax = axes[0, 0]
            polarities = [s['polarity'] for s in sentiments]
            window = 50
            if len(polarities) > window:
                rolling = np.convolve(polarities, np.ones(window)/window, mode='valid')
                ax.plot(range(len(rolling)), rolling, 'b-', linewidth=1)
                ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
                ax.fill_between(range(len(rolling)), rolling, 0, alpha=0.3)
            ax.set_xlabel('Post Index')
            ax.set_ylabel('Polarity (rolling avg)')
            ax.set_title('Sentiment Over Time (-1=negative, +1=positive)')

            # Sentiment distribution
            ax = axes[0, 1]
            ax.hist(polarities, bins=40, edgecolor='black', alpha=0.7)
            ax.axvline(np.mean(polarities), color='r', linestyle='--', label=f'Mean: {np.mean(polarities):.3f}')
            ax.set_xlabel('Polarity')
            ax.set_ylabel('Frequency')
            ax.set_title('Sentiment Distribution')
            ax.legend()

            # Main author sentiment over time
            ax = axes[1, 0]
            author_sent = [s for s in sentiments if s['author'] == main_author]
            if author_sent:
                author_pol = [s['polarity'] for s in author_sent]
                if len(author_pol) > window:
                    rolling = np.convolve(author_pol, np.ones(window)/window, mode='valid')
                    ax.plot(range(len(rolling)), rolling, 'purple', linewidth=1)
                    ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
                ax.set_xlabel('Post Index')
                ax.set_ylabel('Polarity (rolling avg)')
                ax.set_title(f'{main_author} Sentiment Over Time')

            # Subjectivity distribution
            ax = axes[1, 1]
            subj = [s['subjectivity'] for s in sentiments]
            ax.hist(subj, bins=40, edgecolor='black', alpha=0.7, color='orange')
            ax.axvline(np.mean(subj), color='r', linestyle='--', label=f'Mean: {np.mean(subj):.3f}')
            ax.set_xlabel('Subjectivity')
            ax.set_ylabel('Frequency')
            ax.set_title('Subjectivity Distribution (0=objective, 1=subjective)')
            ax.legend()

            plt.tight_layout()
            pdf.savefig(fig)
            plt.close()

        # Page 4: Summary statistics as text
        fig = plt.figure(figsize=(11, 8.5))
        ax = fig.add_subplot(111)
        ax.axis('off')

        # Calculate date range
        timestamps = [p['timestamp'] for p in posts if p['timestamp']]
        date_range = f"{min(timestamps).strftime('%Y-%m-%d')} to {max(timestamps).strftime('%Y-%m-%d')}" if timestamps else "Unknown"
        duration_days = (max(timestamps) - min(timestamps)).days if timestamps else 0

        summary = f"""
WILMOTT THREAD ANALYSIS SUMMARY
{'='*50}

Thread: "Breakthrough in the Theory of Stochastic Differential Equations"

BASIC STATISTICS
----------------
Total Posts: {len(posts):,}
Unique Authors: {len(author_stats):,}
Date Range: {date_range}
Duration: {duration_days:,} days ({duration_days/365:.1f} years)
Average Posts/Day: {len(posts)/max(1,duration_days):.1f}

TOP 5 CONTRIBUTORS
------------------
"""
        for i, (author, stats) in enumerate(sorted(author_stats.items(), key=lambda x: -x[1]['count'])[:5], 1):
            summary += f"{i}. {author}: {stats['count']:,} posts ({100*stats['count']/len(posts):.1f}%)\n"

        summary += f"""
MAIN AUTHOR: {main_author}
------------------
Posts: {author_stats[main_author]['count']:,}
Average Post Length: {author_stats[main_author]['avg_length']:.0f} characters
First Post: {author_stats[main_author]['first_post'].strftime('%Y-%m-%d') if author_stats[main_author]['first_post'] else 'N/A'}
Last Post: {author_stats[main_author]['last_post'].strftime('%Y-%m-%d') if author_stats[main_author]['last_post'] else 'N/A'}

TOP TECHNICAL TERMS
-------------------
"""
        tech_totals = {term: sum(months.values()) for term, months in tech_usage.items()}
        for term, count in sorted(tech_totals.items(), key=lambda x: -x[1])[:10]:
            summary += f"  {term}: {count:,} mentions\n"

        if sentiments:
            author_sent = [s for s in sentiments if s['author'] == main_author]
            summary += f"""
SENTIMENT (Main Author)
-----------------------
Average Polarity: {np.mean([s['polarity'] for s in author_sent]):.3f} (-1 to +1)
Average Subjectivity: {np.mean([s['subjectivity'] for s in author_sent]):.3f} (0 to 1)
"""

        ax.text(0.05, 0.95, summary, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', fontfamily='monospace')

        pdf.savefig(fig)
        plt.close()

    print(f"Report saved to {output_path}")


def main():
    print("Parsing posts from raw HTML...")
    posts = parse_posts()
    print(f"Found {len(posts)} posts")

    if not posts:
        print("No posts found!")
        return

    create_pdf_report(posts, OUTPUT_PDF)
    print(f"\nDone! Output: {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
