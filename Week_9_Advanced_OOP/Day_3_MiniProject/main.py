class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    @staticmethod
    def basic_attack(enemy):
        enemy.life -= 1


class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f'{self.name}: Wielding the power of nature!')

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, enemy):
        enemy.life -= self.attack * 0.5


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f'{self.name}: Slayer of dragons, rescuer of princesses!')

    def brawl(self, enemy):
        self.life += self.attack * 0.5
        enemy.life -= 2 * self.attack

    def train(self):
        self.attack += 2
        self.life += 2

    @staticmethod
    def roar(enemy):
        enemy.attack -= 3


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f'{self.name}: Devoting life to the study and practice of spell casting!')

    def summon(self):
        self.attack += 3

    def cast_spell(self, enemy):
        enemy.life -= self.attack / self.life

    @staticmethod
    def curse(enemy):
        enemy.attack -= 3


amaris = Druid('Amaris')
milcah = Druid('Milcah')

amaris.fight(milcah)
print(milcah.life)

amaris.basic_attack(milcah)
print(milcah.life)

milcah.meditate()
print(milcah.life)

milcah.animal_help()
print(milcah.attack)
milcah.fight(amaris)
print(amaris.life)

phoenix = Warrior('Phoenix')
orion = Warrior('Orion')

phoenix.brawl(orion)
print(phoenix.life)
print(orion.life)

phoenix.train()
print(phoenix.life)
print(phoenix.attack)

phoenix.roar(orion)
print(orion.attack)

arin = Mage('Arin')
imari = Mage('Imari')

arin.curse(amaris)
print(amaris.attack)
