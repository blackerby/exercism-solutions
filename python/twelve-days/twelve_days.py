GIFTS = [
    'twelve Drummers Drumming, ',
    'eleven Pipers Piping, ',
    'ten Lords-a-Leaping, ',
    'nine Ladies Dancing, ',
    'eight Maids-a-Milking, ',
    'seven Swans-a-Swimming, ',
    'six Geese-a-Laying, ',
    'five Gold Rings, ',
    'four Calling Birds, ',
    'three French Hens, ',
    'two Turtle Doves, and ',
    'a Partridge in a Pear Tree.'
]


ORDINALS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
]


def recite(start_verse, end_verse):
    return [build_verse(n) for n in range(start_verse, end_verse+1)]


def build_verse(verse):
    preface = (f"On the {ORDINALS[verse-1]} day of Christmas "
                "my true love gave to me: ")
    gifts = ''.join(GIFTS[len(GIFTS)-verse:])
    return ''.join([preface, gifts])
