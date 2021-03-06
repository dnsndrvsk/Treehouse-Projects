import random
from combat import Combat

COLORS = ['red', 'yellow', 'green', 'blue']


class Monster(Combat):
    min_hp = 1
    max_hp = 1
    min_exp = 1
    max_exp = 1
    weapon = 'sword'
    sound = 'ROAR'
    dmg = 1

    def __init__(self, **kwargs):
        self.hp = random.randint(self.min_hp, self.max_hp)
        self.bloodied = int(self.hp / 2)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        temp = "{} {}, HP: {}, XP: {}"
        return temp.format(self.color.title(),
                           self.__class__.__name__,
                           self.hp,
                           self.exp)

    def battlecry(self):
        return self.sound.upper()


class Goblin(Monster):
    max_hp = 3
    max_exp = 2
    dmg = 1
    sound = 'squeak'


class Troll(Monster):
    min_hp = 3
    max_hp = 5
    min_exp = 3
    max_exp = 6
    dmg = 2
    sound = 'growl'


class Dragon(Monster):
    min_hp = 5
    max_hp = 10
    min_exp = 6
    max_exp = 10
    dmg = 3
    sound = 'rooooaaaaar'
