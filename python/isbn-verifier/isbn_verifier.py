def is_valid(isbn):
    tokens = list(isbn.replace('-', ''))
    if len(tokens) != 10:
        return False
    for i, n in enumerate(tokens):
        if n.isnumeric():
            tokens[i] = int(n)
        elif n == 'X' and i == 9:
            tokens[i] = 10
    if any(isinstance(t, str) for t in tokens):
        return False
    return sum(x * i for x, i in zip(tokens, range(10, 0, -1))) % 11 == 0
