class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='Anonymous', age=0):
        if PlayerCharacter.membership and (age > 18):  # self..membership:
            self.name = name  # Object Attribute
            self.age = age

    # Instance methods
    def run(self):
        print('Running...')

    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def sum(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Joeri', 35)
print(player1.name)
print(player1.age)
player1.run()

player1.attack = 50
print(player1.attack)

print(player1.membership)
player1.shout()

player2 = PlayerCharacter()
# print(player2.name)
# print(player2.age)
# player2.shout()

player3 = PlayerCharacter.adding_things(2, 3)
#print(player3.name)
print(player3.sum(2, 3))
