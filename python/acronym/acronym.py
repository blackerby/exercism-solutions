import re


def abbreviate(words):
    words = re.findall(r"([A-Z']+)", words.upper())
    return ''.join(word[0] for word in words)
