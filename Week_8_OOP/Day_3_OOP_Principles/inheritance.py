
# INHERITANCE

"""Inheritance is when a class uses code constructed within another class. Classes called child classes or subclasses
inherit methods and variables from parent classes or base classes. """


class Animal():
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def bark(self):
        print(f'{self.name} barked, WAF!')


my_dog = Dog('Rex')
my_dog.bark()


class Vehicle():

    def turn_right(self):
        print('Turning Right')

    def turn_left(self):
        print('Turning Left')

    def speed(self):
        print('Speeding')


class Car(Vehicle):
    pass


my_car = Car()
my_car.speed()

# OVERRIDING PARENT METHODS
"""When you create the same method inside the child class, you override the parent class method. It’s important to 
note that child classes override or extend the functionality of parent classes. The child class will have all the 
parent class’s functions, plus his functions. """

class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")


class Dog(Animal):
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")

    def make_sound(self):
        print("I am an DOGGG !!! WOUAFFF!!")


rex = Dog('dog', 4, "Wouaf")
rex.make_sound()
# >> I am an DOGGG !!! WOUAFFF!!


# The Super() function
"""
With the super() function, you can gain access to inherited methods that have been overwritten in a class object.
"""
class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):
    def __init__(self, type, number_legs, sound, fetch_ball):
        super().__init__(type, number_legs, sound)
        # Or : Animal.__init__(self,type, number_legs, sound)
        self.fetch_ball = fetch_ball


rex = Dog('dog', 4, "wouaf", True)
print('This animal is a:', rex.type)
# >> This animal is a dog

print('This dog has', rex.number_legs , ' legs')
# >> This dog has 4 legs

print('This dog makes the sound ', rex.sound)
# >> This dog makes the sound wouaf

print('Does this dog fetch balls ? ', rex.fetch_ball)
# >> Does this dog fetch balls ? True

"""We use super() function before __init__() method. We want to pull the content of __init__() method from the parent 
class into the child class. You can also specify from which class you want to use the super() function. """

class MyClass(object):
    def func(self):
        print("I'm being called from the Parent class")


class ChildClass(MyClass):
    def func(self):
        print("I'm actually being called from the Child class")
        print("But...")
        # Calling the `func()` method from the Parent class.
        super(ChildClass, self).func()


my_instance_2 = ChildClass()
my_instance_2.func()
