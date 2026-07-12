#!/usr/bin/env python3
"""Build a monthly posting-rate chart from the archived Wilmott HTML."""

from collections import Counter
from datetime import datetime
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from analyze_thread import parse_posts


OUTPUT = Path("assets/posting_rate.png")


def month_range(start: datetime, end: datetime) -> list[datetime]:
    months: list[datetime] = []
    current = datetime(start.year, start.month, 1)
    final = datetime(end.year, end.month, 1)
    while current <= final:
        months.append(current)
        if current.month == 12:
            current = datetime(current.year + 1, 1, 1)
        else:
            current = datetime(current.year, current.month + 1, 1)
    return months


def monthly_post_counts() -> tuple[list[datetime], list[int]]:
    posts = parse_posts()
    dated_posts = [post["timestamp"] for post in posts if post["timestamp"]]
    counts = Counter(date.strftime("%Y-%m") for date in dated_posts)
    months = month_range(min(dated_posts), max(dated_posts))
    monthly_counts = [counts.get(month.strftime("%Y-%m"), 0) for month in months]
    return months, monthly_counts


def build_chart(output: Path = OUTPUT) -> None:
    months, counts = monthly_post_counts()
    peak_count = max(counts)
    peak_date = months[counts.index(peak_count)]

    background = "#f5f1e8"
    ink = "#183b3a"
    line = "#147d74"
    fill = "#70b8aa"
    grid = "#d9d3c5"

    with plt.rc_context(
        {
            "font.family": "DejaVu Sans",
            "axes.facecolor": background,
            "figure.facecolor": background,
            "axes.edgecolor": ink,
            "axes.labelcolor": ink,
            "xtick.color": ink,
            "ytick.color": ink,
            "text.color": ink,
        }
    ):
        fig, ax = plt.subplots(figsize=(16, 7), dpi=160)
        ax.fill_between(months, counts, color=fill, alpha=0.35)
        ax.plot(months, counts, color=line, linewidth=2.2)
        ax.scatter([peak_date], [peak_count], color=ink, s=34, zorder=3)
        ax.annotate(
            f"Peak: {peak_count} posts\n{peak_date:%B %Y}",
            xy=(peak_date, peak_count),
            xytext=(18, -12),
            textcoords="offset points",
            ha="left",
            va="top",
            fontsize=10,
            color=ink,
        )

        ax.set_title(
            "Posting rate in the Wilmott ‘Breakthrough in SDEs’ thread",
            loc="left",
            fontsize=20,
            fontweight="normal",
            pad=18,
        )
        ax.text(
            0,
            1.01,
            "Monthly posts · April 2016–January 2026",
            transform=ax.transAxes,
            fontsize=11,
            color="#4f6662",
            ha="left",
        )
        ax.set_xlabel("Date", labelpad=12)
        ax.set_ylabel("Number of posts", labelpad=12)
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
        ax.set_xlim(min(months), max(months))
        ax.set_ylim(bottom=0)
        ax.grid(axis="y", color=grid, linewidth=0.8)
        ax.grid(axis="x", visible=False)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(grid)
        ax.spines["bottom"].set_color(grid)
        ax.margins(x=0)

        fig.tight_layout()
        fig.savefig(output, bbox_inches="tight", facecolor=background)
        plt.close(fig)


if __name__ == "__main__":
    build_chart()
