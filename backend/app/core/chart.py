import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os
import tempfile
from .data_types import WordCounts

def create_bar_chart(word_counts: WordCounts):
    """Create a horizontal bar chart of word counts."""
    words = list(word_counts.word_counts.keys())
    counts = list(word_counts.word_counts.values())

    plt.figure(figsize=(10, 8))
    y_pos = np.arange(len(words))
    plt.barh(y_pos, counts)
    plt.yticks(y_pos, words)
    plt.xlabel("Counts")
    plt.title("Word Counts Bar Chart")
    plt.gca().invert_yaxis()

    plt.tight_layout()
    chart_path = os.path.join(tempfile.gettempdir(), "bar_chart.png")
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def create_pie_chart(word_counts: WordCounts):
    """Create a pie chart of word counts."""
    words = list(word_counts.word_counts.keys())
    counts = list(word_counts.word_counts.values())

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=words, autopct="%1.1f%%", startangle=140)
    plt.title("Word Counts Pie Chart")

    plt.tight_layout()
    chart_path = os.path.join(tempfile.gettempdir(), "pie_chart.png")
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def create_line_chart(word_counts: WordCounts):
    """Create a line chart of word counts."""
    words = list(word_counts.word_counts.keys())
    counts = list(word_counts.word_counts.values())

    plt.figure(figsize=(10, 6))
    plt.plot(words, counts, marker="o")
    plt.xticks(rotation=90)
    plt.xlabel("Words")
    plt.ylabel("Counts")
    plt.title("Word Counts Line Chart")

    plt.tight_layout()
    chart_path = os.path.join(tempfile.gettempdir(), "line_chart.png")
    plt.savefig(chart_path)
    plt.close()
    return chart_path
