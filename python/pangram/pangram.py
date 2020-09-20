from collections import Counter

def is_pangram(sentence):
    return len(Counter([c for c in sentence.lower() if c.isalpha()])) == 26
