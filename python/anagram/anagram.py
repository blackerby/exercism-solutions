def find_anagrams(word, candidates):
    return [
        cand
        for cand in candidates
        if word.lower() != cand.lower()
        if sorted(word.lower()) == sorted(cand.lower())
    ]
