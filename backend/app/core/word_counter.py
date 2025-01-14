import re
from typing import Dict
from .data_types import WordCounts
from .constants import COMMON_WORDS_BLACKLIST

def word_counter(script: str, min_count_threshold: int = 10) -> WordCounts:
    """
    Counts the frequency of each word in the script, filters out common words,
    and returns word counts greater than the specified threshold.
    """
    # Remove punctuation and make all words lowercase
    script = re.sub(r'[^\w\s]', '', script)
    script = script.lower()

    # Split script into words
    words = script.split()

    # Filter out common words
    words = [word for word in words if word not in COMMON_WORDS_BLACKLIST]

    # Count word frequencies
    word_counts_dict = {}
    for word in words:
        word_counts_dict[word] = word_counts_dict.get(word, 0) + 1

    # Filter words by min_count_threshold
    word_counts_filtered = {word: count for word, count in word_counts_dict.items() 
                          if count > min_count_threshold}

    # Sort descending by count
    word_counts_sorted = dict(sorted(word_counts_filtered.items(), 
                                   key=lambda item: item[1], reverse=True))

    # Return WordCounts object
    return WordCounts(word_counts=word_counts_sorted)
