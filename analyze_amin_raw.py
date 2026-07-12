#!/usr/bin/env python3
"""
Generate raw stats about Amin's posting behavior.
Output text for review, then we'll pick interesting bits for PDF.
"""

import re
import json
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timedelta
import numpy as np

try:
    from textblob import TextBlob
    HAS_TEXTBLOB = True
except:
    HAS_TEXTBLOB = False

RAW_DIR = Path("./raw")

def parse_posts():
    """Extract posts with metadata from raw HTML files."""
    posts = []
    html_files = sorted(RAW_DIR.glob("page_start_*.html"))

    post_pattern = re.compile(
        r'<a class="icon_post_target"[^>]*>#(\d+)</a>.*?'
        r'<span class="timestamp">([^<]+)</span>.*?'
        r'<div class="content">(.*?)</div>\s*(?=<div class="back2top|<div class="post|<div class="notice|$)',
        re.DOTALL
    )

    author_pattern = re.compile(
        r'<a[^>]*class="username"[^>]*>([^<]+)</a>.*?'
        r'<a class="icon_post_target"[^>]*>#(\d+)</a>',
        re.DOTALL
    )

    seen = set()
    for html_file in html_files:
        content = html_file.read_text(encoding='utf-8')

        author_map = {}
        for match in author_pattern.finditer(content):
            author_map[int(match.group(2))] = match.group(1).strip()

        for match in post_pattern.finditer(content):
            post_num = int(match.group(1))
            if post_num in seen:
                continue
            seen.add(post_num)

            timestamp_str = match.group(2).strip()
            post_content = match.group(3)

            timestamp = None
            try:
                ts = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', timestamp_str)
                timestamp = datetime.strptime(ts, '%B %d, %Y, %I:%M %p')
            except:
                pass

            # Keep raw HTML for code detection, clean version for text analysis
            text_clean = re.sub(r'<[^>]+>', ' ', post_content)
            text_clean = re.sub(r'&[a-z]+;', ' ', text_clean)
            text_clean = re.sub(r'\s+', ' ', text_clean).strip()

            # Detect code blocks
            has_code = bool(re.search(r'<pre|<code|```', post_content))

            # Count equations
            equation_count = post_content.count('[$]') // 2  # pairs

            posts.append({
                'num': post_num,
                'author': author_map.get(post_num, 'Unknown'),
                'timestamp': timestamp,
                'text': text_clean,
                'raw_html': post_content,
                'length': len(text_clean),
                'has_code': has_code,
                'equation_count': equation_count
            })

    posts.sort(key=lambda p: p['num'])
    return posts


def strip_code_and_math(text):
    """Remove code blocks and LaTeX for pure language analysis."""
    # Remove LaTeX
    text = re.sub(r'\[\$\].*?\[\$\]', ' ', text, flags=re.DOTALL)
    text = re.sub(r'\$[^$]+\$', ' ', text)
    # Remove common code patterns
    text = re.sub(r'\b(function|end|for|if|else|while|return|int|double|float)\b', ' ', text)
    text = re.sub(r'[{};=\[\]()]+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def analyze_temporal(posts):
    """Temporal patterns."""
    stats = {
        'by_hour': Counter(),
        'by_15min': Counter(),
        'by_day_of_week': Counter(),
        'by_year_month': Counter(),
        'by_year': Counter(),
        'weekend_vs_weekday': {'weekend': 0, 'weekday': 0},
        'posts_per_day': defaultdict(int),
        'streaks': [],
        'gaps': [],
    }

    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    prev_date = None
    streak = 0

    for post in posts:
        if not post['timestamp']:
            continue
        ts = post['timestamp']

        stats['by_hour'][ts.hour] += 1
        stats['by_15min'][f"{ts.hour:02d}:{(ts.minute//15)*15:02d}"] += 1
        stats['by_day_of_week'][day_names[ts.weekday()]] += 1
        stats['by_year_month'][ts.strftime('%Y-%m')] += 1
        stats['by_year'][ts.year] += 1

        if ts.weekday() >= 5:
            stats['weekend_vs_weekday']['weekend'] += 1
        else:
            stats['weekend_vs_weekday']['weekday'] += 1

        date = ts.date()
        stats['posts_per_day'][str(date)] += 1

        if prev_date:
            gap = (date - prev_date).days
            if gap == 0 or gap == 1:
                streak += 1
            else:
                if streak > 1:
                    stats['streaks'].append(streak)
                stats['gaps'].append(gap)
                streak = 1
        else:
            streak = 1
        prev_date = date

    if streak > 1:
        stats['streaks'].append(streak)

    # Convert Counters to dicts for JSON
    stats['by_hour'] = dict(stats['by_hour'])
    stats['by_15min'] = dict(sorted(stats['by_15min'].items()))
    stats['by_day_of_week'] = dict(stats['by_day_of_week'])
    stats['by_year_month'] = dict(sorted(stats['by_year_month'].items()))
    stats['by_year'] = dict(sorted(stats['by_year'].items()))

    # Summary stats
    posts_per_day_vals = list(stats['posts_per_day'].values())
    stats['posts_per_day_summary'] = {
        'max': max(posts_per_day_vals),
        'mean': np.mean(posts_per_day_vals),
        'median': np.median(posts_per_day_vals),
        'days_with_10plus': sum(1 for v in posts_per_day_vals if v >= 10),
    }
    stats['streak_summary'] = {
        'max': max(stats['streaks']) if stats['streaks'] else 0,
        'mean': np.mean(stats['streaks']) if stats['streaks'] else 0,
    }
    stats['gap_summary'] = {
        'max': max(stats['gaps']) if stats['gaps'] else 0,
        'mean': np.mean(stats['gaps']) if stats['gaps'] else 0,
        'gaps_over_7_days': sum(1 for g in stats['gaps'] if g > 7),
    }

    del stats['posts_per_day']  # Too big for output
    del stats['streaks']
    del stats['gaps']

    return stats


def analyze_language(posts):
    """Language patterns."""
    stats = {
        'total_words': 0,
        'unique_words': set(),
        'word_counts': Counter(),
        'bigrams': Counter(),

        # LIWC-style categories
        'certainty_words': Counter(),  # always, never, definitely, clearly
        'tentative_words': Counter(),  # maybe, perhaps, might, possibly
        'absolutist_words': Counter(),  # nothing, everything, completely
        'cognitive_words': Counter(),  # think, know, understand, realize
        'achievement_words': Counter(),  # breakthrough, success, solved, perfect
        'social_words': Counter(),  # friends, we, colleagues
        'negative_words': Counter(),  # wrong, error, mistake, fail
        'positive_words': Counter(),  # good, great, excellent, correct

        # Pronouns
        'first_person_singular': 0,  # I, me, my, mine
        'first_person_plural': 0,  # we, us, our
        'second_person': 0,  # you, your

        # Markers
        'questions': 0,
        'exclamations': 0,
        'hedging_phrases': Counter(),
        'defensive_phrases': Counter(),

        # By year
        'by_year': defaultdict(lambda: {
            'words': 0,
            'unique': set(),
            'certainty': 0,
            'tentative': 0,
            'i_count': 0,
            'we_count': 0,
        }),
    }

    certainty = {'always', 'never', 'definitely', 'certainly', 'clearly', 'obviously', 'absolutely', 'undoubtedly'}
    tentative = {'maybe', 'perhaps', 'might', 'possibly', 'probably', 'seems', 'appears', 'suggest'}
    absolutist = {'nothing', 'everything', 'completely', 'totally', 'entirely', 'impossible', 'always', 'never'}
    cognitive = {'think', 'know', 'understand', 'realize', 'believe', 'consider', 'suppose', 'assume'}
    achievement = {'breakthrough', 'success', 'solved', 'perfect', 'excellent', 'achieved', 'accomplished', 'discovered'}
    social = {'friends', 'colleagues', 'everyone', 'community', 'together', 'share'}
    negative = {'wrong', 'error', 'mistake', 'fail', 'failed', 'incorrect', 'problem', 'issue', 'bad'}
    positive = {'good', 'great', 'excellent', 'correct', 'right', 'nice', 'well', 'better', 'best'}

    hedging = ['i think', 'in my opinion', 'it seems', 'i believe', 'i suppose', 'i guess', 'not sure']
    defensive = ['as i said', 'as i mentioned', 'i already', 'if you read', 'i have explained', 'actually', 'in fact']

    for post in posts:
        if not post['timestamp']:
            continue

        year = post['timestamp'].year
        text = strip_code_and_math(post['text']).lower()
        words = re.findall(r'\b[a-z]{2,}\b', text)

        stats['total_words'] += len(words)
        stats['unique_words'].update(words)
        stats['word_counts'].update(words)

        stats['by_year'][year]['words'] += len(words)
        stats['by_year'][year]['unique'].update(words)

        for i in range(len(words) - 1):
            stats['bigrams'][(words[i], words[i+1])] += 1

        # Categories
        for w in words:
            if w in certainty:
                stats['certainty_words'][w] += 1
                stats['by_year'][year]['certainty'] += 1
            if w in tentative:
                stats['tentative_words'][w] += 1
                stats['by_year'][year]['tentative'] += 1
            if w in absolutist:
                stats['absolutist_words'][w] += 1
            if w in cognitive:
                stats['cognitive_words'][w] += 1
            if w in achievement:
                stats['achievement_words'][w] += 1
            if w in social:
                stats['social_words'][w] += 1
            if w in negative:
                stats['negative_words'][w] += 1
            if w in positive:
                stats['positive_words'][w] += 1

        # Pronouns
        i_words = len(re.findall(r'\b(i|me|my|mine|myself)\b', text))
        we_words = len(re.findall(r'\b(we|us|our|ours|ourselves)\b', text))
        you_words = len(re.findall(r'\b(you|your|yours|yourself)\b', text))

        stats['first_person_singular'] += i_words
        stats['first_person_plural'] += we_words
        stats['second_person'] += you_words
        stats['by_year'][year]['i_count'] += i_words
        stats['by_year'][year]['we_count'] += we_words

        # Questions and exclamations
        stats['questions'] += text.count('?')
        stats['exclamations'] += text.count('!')

        # Phrases
        for phrase in hedging:
            if phrase in text:
                stats['hedging_phrases'][phrase] += 1
        for phrase in defensive:
            if phrase in text:
                stats['defensive_phrases'][phrase] += 1

    # Convert for output
    stats['unique_words'] = len(stats['unique_words'])
    stats['lexical_diversity'] = stats['unique_words'] / stats['total_words'] if stats['total_words'] > 0 else 0

    # Top words (excluding common)
    stop = {'the', 'and', 'that', 'this', 'with', 'for', 'are', 'but', 'not', 'you', 'have', 'has',
            'was', 'will', 'can', 'would', 'could', 'should', 'from', 'they', 'been', 'were', 'which',
            'there', 'their', 'what', 'about', 'when', 'into', 'than', 'then', 'also', 'its', 'just',
            'over', 'such', 'after', 'most', 'only', 'other', 'new', 'some', 'could', 'time', 'very',
            'these', 'may', 'more', 'out', 'all', 'being', 'where'}
    stats['top_words'] = [(w, c) for w, c in stats['word_counts'].most_common(200) if w not in stop][:50]
    stats['top_bigrams'] = [(f"{b[0]} {b[1]}", c) for b, c in stats['bigrams'].most_common(100)
                           if b[0] not in stop and b[1] not in stop][:30]

    stats['certainty_words'] = dict(stats['certainty_words'].most_common(20))
    stats['tentative_words'] = dict(stats['tentative_words'].most_common(20))
    stats['absolutist_words'] = dict(stats['absolutist_words'].most_common(20))
    stats['cognitive_words'] = dict(stats['cognitive_words'].most_common(20))
    stats['achievement_words'] = dict(stats['achievement_words'].most_common(20))
    stats['social_words'] = dict(stats['social_words'].most_common(20))
    stats['negative_words'] = dict(stats['negative_words'].most_common(20))
    stats['positive_words'] = dict(stats['positive_words'].most_common(20))
    stats['hedging_phrases'] = dict(stats['hedging_phrases'].most_common(20))
    stats['defensive_phrases'] = dict(stats['defensive_phrases'].most_common(20))

    # By year summary
    by_year_clean = {}
    for year, data in sorted(stats['by_year'].items()):
        by_year_clean[year] = {
            'words': data['words'],
            'unique': len(data['unique']),
            'lexical_diversity': len(data['unique']) / data['words'] if data['words'] > 0 else 0,
            'certainty': data['certainty'],
            'tentative': data['tentative'],
            'certainty_ratio': data['certainty'] / (data['certainty'] + data['tentative']) if (data['certainty'] + data['tentative']) > 0 else 0,
            'i_count': data['i_count'],
            'we_count': data['we_count'],
            'i_vs_we_ratio': data['i_count'] / (data['i_count'] + data['we_count']) if (data['i_count'] + data['we_count']) > 0 else 0,
        }
    stats['by_year'] = by_year_clean

    del stats['word_counts']
    del stats['bigrams']

    return stats


def analyze_sentiment(posts):
    """Sentiment analysis."""
    if not HAS_TEXTBLOB:
        return {'error': 'textblob not installed'}

    stats = {
        'overall': {'polarity': [], 'subjectivity': []},
        'by_year': defaultdict(lambda: {'polarity': [], 'subjectivity': []}),
        'by_month': defaultdict(lambda: {'polarity': [], 'subjectivity': []}),
        'extremes': {'most_positive': [], 'most_negative': []},
    }

    for post in posts:
        if not post['timestamp']:
            continue

        text = strip_code_and_math(post['text'])
        if len(text) < 50:
            continue

        blob = TextBlob(text[:3000])
        pol = blob.sentiment.polarity
        subj = blob.sentiment.subjectivity

        stats['overall']['polarity'].append(pol)
        stats['overall']['subjectivity'].append(subj)

        year = post['timestamp'].year
        month = post['timestamp'].strftime('%Y-%m')

        stats['by_year'][year]['polarity'].append(pol)
        stats['by_year'][year]['subjectivity'].append(subj)
        stats['by_month'][month]['polarity'].append(pol)
        stats['by_month'][month]['subjectivity'].append(subj)

        stats['extremes']['most_positive'].append((pol, post['num'], text[:100]))
        stats['extremes']['most_negative'].append((pol, post['num'], text[:100]))

    # Summarize
    stats['overall'] = {
        'polarity_mean': np.mean(stats['overall']['polarity']),
        'polarity_std': np.std(stats['overall']['polarity']),
        'subjectivity_mean': np.mean(stats['overall']['subjectivity']),
        'subjectivity_std': np.std(stats['overall']['subjectivity']),
    }

    by_year_clean = {}
    for year, data in sorted(stats['by_year'].items()):
        by_year_clean[year] = {
            'polarity_mean': np.mean(data['polarity']),
            'polarity_std': np.std(data['polarity']),
            'subjectivity_mean': np.mean(data['subjectivity']),
            'n_posts': len(data['polarity']),
        }
    stats['by_year'] = by_year_clean

    # Monthly for trend
    by_month_clean = {}
    for month, data in sorted(stats['by_month'].items()):
        by_month_clean[month] = {
            'polarity_mean': np.mean(data['polarity']),
            'n_posts': len(data['polarity']),
        }
    stats['by_month'] = by_month_clean

    # Extremes
    stats['extremes']['most_positive'] = sorted(stats['extremes']['most_positive'], reverse=True)[:5]
    stats['extremes']['most_negative'] = sorted(stats['extremes']['most_negative'])[:5]

    return stats


def analyze_content_patterns(posts):
    """Content-specific patterns."""
    stats = {
        'equation_density': [],  # equations per post over time
        'code_posts': 0,
        'avg_post_length': [],
        'length_by_year': defaultdict(list),
        'self_references': 0,  # "as I mentioned", "post #X"
        'quotes_others': 0,  # quoting other users
    }

    for post in posts:
        if not post['timestamp']:
            continue

        year = post['timestamp'].year

        stats['equation_density'].append(post['equation_count'])
        stats['code_posts'] += 1 if post['has_code'] else 0
        stats['avg_post_length'].append(post['length'])
        stats['length_by_year'][year].append(post['length'])

        text_lower = post['text'].lower()
        if re.search(r'(as i (said|mentioned|explained)|post #\d+|in my (previous|earlier))', text_lower):
            stats['self_references'] += 1
        if 'originally posted by' in text_lower or 'quote' in post['raw_html'].lower()[:500]:
            stats['quotes_others'] += 1

    stats['equation_density_mean'] = np.mean(stats['equation_density'])
    stats['equation_density_max'] = max(stats['equation_density'])
    stats['posts_with_equations'] = sum(1 for e in stats['equation_density'] if e > 0)

    stats['length_mean'] = np.mean(stats['avg_post_length'])
    stats['length_std'] = np.std(stats['avg_post_length'])
    stats['length_max'] = max(stats['avg_post_length'])

    length_by_year_clean = {}
    for year, lengths in sorted(stats['length_by_year'].items()):
        length_by_year_clean[year] = {
            'mean': np.mean(lengths),
            'max': max(lengths),
            'n_posts': len(lengths),
        }
    stats['length_by_year'] = length_by_year_clean

    del stats['equation_density']
    del stats['avg_post_length']

    return stats


def analyze_interactions(all_posts, amin_posts):
    """How Amin interacts with others."""
    stats = {
        'response_rate': 0,  # % of non-Amin posts followed by Amin reply
        'avg_response_time_hours': [],
        'sentiment_after_others': [],
        'sentiment_standalone': [],
    }

    # Build timeline
    all_sorted = sorted([p for p in all_posts if p['timestamp']], key=lambda p: p['timestamp'])

    other_posts = 0
    amin_responses = 0

    for i, post in enumerate(all_sorted):
        if post['author'] != 'Amin':
            other_posts += 1
            # Check if next post is Amin
            if i + 1 < len(all_sorted) and all_sorted[i+1]['author'] == 'Amin':
                amin_responses += 1
                # Response time
                delta = (all_sorted[i+1]['timestamp'] - post['timestamp']).total_seconds() / 3600
                if delta < 168:  # within a week
                    stats['avg_response_time_hours'].append(delta)

    stats['response_rate'] = amin_responses / other_posts if other_posts > 0 else 0
    stats['avg_response_time'] = np.mean(stats['avg_response_time_hours']) if stats['avg_response_time_hours'] else 0
    stats['median_response_time'] = np.median(stats['avg_response_time_hours']) if stats['avg_response_time_hours'] else 0
    del stats['avg_response_time_hours']
    del stats['sentiment_after_others']
    del stats['sentiment_standalone']

    return stats


def main():
    print("Parsing posts...")
    all_posts = parse_posts()
    amin_posts = [p for p in all_posts if p['author'] == 'Amin']
    print(f"Found {len(all_posts)} total posts, {len(amin_posts)} from Amin")

    results = {
        'summary': {
            'total_posts': len(all_posts),
            'amin_posts': len(amin_posts),
            'amin_percentage': len(amin_posts) / len(all_posts) * 100,
            'date_range': {
                'start': min(p['timestamp'] for p in amin_posts if p['timestamp']).isoformat(),
                'end': max(p['timestamp'] for p in amin_posts if p['timestamp']).isoformat(),
            }
        }
    }

    print("Analyzing temporal patterns...")
    results['temporal'] = analyze_temporal(amin_posts)

    print("Analyzing language...")
    results['language'] = analyze_language(amin_posts)

    print("Analyzing sentiment...")
    results['sentiment'] = analyze_sentiment(amin_posts)

    print("Analyzing content patterns...")
    results['content'] = analyze_content_patterns(amin_posts)

    print("Analyzing interactions...")
    results['interactions'] = analyze_interactions(all_posts, amin_posts)

    # Output
    output = Path("./amin_analysis_raw.txt")
    with open(output, 'w') as f:
        f.write("AMIN ANALYSIS - RAW STATS\n")
        f.write("=" * 60 + "\n\n")

        def write_section(name, data, indent=0):
            prefix = "  " * indent
            if isinstance(data, dict):
                f.write(f"{prefix}{name}:\n")
                for k, v in data.items():
                    write_section(str(k), v, indent + 1)
            elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], tuple):
                f.write(f"{prefix}{name}:\n")
                for item in data[:20]:
                    f.write(f"{prefix}  {item}\n")
            elif isinstance(data, float):
                f.write(f"{prefix}{name}: {data:.4f}\n")
            else:
                f.write(f"{prefix}{name}: {data}\n")

        for section, data in results.items():
            f.write(f"\n{'='*60}\n{section.upper()}\n{'='*60}\n")
            write_section(section, data)

    print(f"\nOutput written to {output}")
    print(f"File size: {output.stat().st_size / 1024:.1f}KB")


if __name__ == "__main__":
    main()
