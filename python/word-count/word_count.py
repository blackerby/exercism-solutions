import re
from collections import Counter

def count_words(sentence):
    words = re.findall(r"([0-9a-z]+(?:'[a-z]+)?)", sentence.lower())
    return Counter(words)
