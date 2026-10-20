from random import randint


class Person:
    def __init__(self, name):
        self.name = name
        self.hp = self.compute_hp()
        self.mp = self.compute_mp()
        self.prot = self.compute_prot()
        self.atk = self.compute_atk()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 0:
            self.__name = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value > 0:
            self.__hp = value

    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, value):
        if value > 0:
            self.__mp = value

    @property
    def prot(self):
        return self.__prot

    @prot.setter
    def prot(self, value):
        if value > 0:
            self.__prot = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if value > 0:
            self.__atk = value

    def attack(self, other):
        while self.hp > 0 and other.hp > 0:
            dammage_self = Attack.compute_dammage(self, other)
            print(f"{self.__name} attaque et fait {dammage_self} dégats")
            other.hp -= dammage_self
            input()

            dammage_other = Attack.compute_dammage(other, self)
            print(f"{other.__name} attaque et fait {dammage_other} dégats")
            self.hp -= dammage_other
            input()

    def heal(self, value):
        self.hp += value

    def compute_hp(self):
        dices = RandomDice.six_dice()
        dices.sort()
        return sum(dices[3:-1])

    def compute_mp(self):
        dices = RandomDice.six_dice()
        dices.sort()
        return sum(dices[3:-1])

    def compute_prot(self):
        dices = RandomDice.six_dice()
        dices.sort()
        return sum(dices[3:-1])

    def compute_atk(self):
        dices = RandomDice.six_dice()
        dices.sort()
        return sum(dices[3:-1])

    def take_level(self):
        self.hp += (self.hp / 100) * 15
        self.mp += (self.hp / 100) * 15
        self.atk += (self.hp / 100) * 15
        self.prot += (self.hp / 100) * 15


class Attack:
    @staticmethod
    def compute_dammage(actif, passif):
        return actif.atk - passif.prot if actif.atk - passif.prot > 0 else 5


class RandomDice:
    @staticmethod
    def three_dice():
        return [randint(1, 6), randint(1, 6), randint(1, 6)]

    @staticmethod
    def six_dice():
        return [
            randint(1, 6),
            randint(1, 6),
            randint(1, 6),
            randint(1, 6),
            randint(1, 6),
            randint(1, 6),
        ]


hero = Person("bob")
monster = Person("monster")

hero.attack(monster)
