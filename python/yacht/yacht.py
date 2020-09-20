from collections import Counter

YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    counter = Counter(dice)
    result = 0
    if category == YACHT and len(counter) == 1:
        result = 50
    elif category == FULL_HOUSE:
        if sorted(counter.values()) == [2,3]:
            result = sum(dice)
    elif category == FOUR_OF_A_KIND:
        for k, v in counter.items():
            if v >= 4:
                result = 4 * k
    elif category == CHOICE:
        result = sum(dice)
    elif category == LITTLE_STRAIGHT and sorted(dice) == list(range(1, 6)):
        result = 30
    elif category == BIG_STRAIGHT and sorted(dice) == list(range(2, 7)):
        result = 30
    elif category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        for k, v in counter.items():
            if k == category:
                result = k*v
    return result
