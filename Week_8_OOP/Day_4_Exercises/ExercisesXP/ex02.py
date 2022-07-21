"""
Exercise 2 : Dogs
Instructions
Create a class called Dog with the following attributes name, age, weight.
Implement the following methods in the Dog class:
bark: returns a string which states: “<dog_name> is barking”.
run_speed: returns the dogs running speed (weight/age*10).
fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating
which dog won the fight. The winner should be the dog with the higher run_speed x weight.

Create 3 dogs and run them through your class.
"""

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking.'

    def run_speed(self):
        return self.weight / (self.age * 10)

    def fight(self, other_dog):
        if (self.run_speed() * self.weight) > (other_dog.run_speed() * other_dog.weight):
            return f'{self.name} won the fight.'
        else:
            return f'{other_dog.name} won the fight.'



dog1 = Dog('dog1', 5, 10)
dog2 = Dog('dog2', 6, 12)
dog3 = Dog('dog3', 7, 13)

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))
