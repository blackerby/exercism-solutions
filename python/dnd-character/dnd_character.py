from random import randint

ABILITIES = ('strength', 'dexterity', 'constitution',
                'intelligence', 'wisdom', 'charisma')

class Character:
    def __init__(self):
        for ability in ABILITIES:
            setattr(self, ability, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        dice = sorted(randint(1, 6) for _ in range(4))
        return sum(dice[1:])


def modifier(constitution):
    return (constitution - 10) // 2
