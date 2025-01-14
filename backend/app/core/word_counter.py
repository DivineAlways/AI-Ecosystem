import re
from typing import Dict
from .data_types import WordCounts
from .constants import COMMON_WORDS_BLACKLIST

def word_counter(script: str, min_count_threshold: int = 10) -> WordCounts:
    """
    Counts the frequency of each word in the script, filters out common words,
    and returns word counts greater than the specified threshold.
    """
    if not script or not script.strip():
        return WordCounts(word_counts={"no_content": 0})

    # Remove punctuation and make all words lowercase
    script = re.sub(r'[^\w\s]', '', script)
    script = script.lower()

    # Split script into words and remove empty strings
    words = [word for word in script.split() if word.strip()]
    
    if not words:
        return WordCounts(word_counts={"no_valid_words": 0})

    # Filter out common words
    words = [word for word in words if word not in COMMON_WORDS_BLACKLIST]
    
    if not words:
        return WordCounts(word_counts={"only_common_words": 0})

    # Count word frequencies
    word_counts_dict = {}
    for word in words:
        word_counts_dict[word] = word_counts_dict.get(word, 0) + 1

    # Filter words by min_count_threshold
    word_counts_filtered = {word: count for word, count in word_counts_dict.items() 
                          if count > min_count_threshold}
    
    if not word_counts_filtered:
        # If no words meet the threshold, return the top 5 most frequent words
        word_counts_sorted = dict(sorted(word_counts_dict.items(), 
                                       key=lambda item: item[1], reverse=True)[:5])
    else:
        # Sort descending by count
        word_counts_sorted = dict(sorted(word_counts_filtered.items(), 
                                       key=lambda item: item[1], reverse=True))

    # Return WordCounts object
    return WordCounts(word_counts=word_counts_sorted)
