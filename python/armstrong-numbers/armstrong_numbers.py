def is_armstrong_number(number):
    digits = list(map(int, str(number)))
    exp = len(digits)
    return sum(map(lambda digit: digit**exp, digits)) == number
