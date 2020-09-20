def factors(value):
    for divisor in range(2, value):
        quotient, remainder = divmod(value, divisor)
