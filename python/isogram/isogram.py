def is_isogram(string):
    string = [char for char in string.lower() if char.isalpha()]
    return len(string) == len(set(string))
