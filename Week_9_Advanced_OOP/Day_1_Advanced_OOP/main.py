# Class Attributes
class Dog:
    counter = 0  # ==> Class Attribute

    def __init__(self, name):
        self.name = name  # ==> Instance Attribute
        Dog.counter += 1  # => Increment the Class attribute


rex = Dog("Rex")
lassy = Dog("Lassy")

print(rex.name)
print(lassy.name)
print(Dog.counter)

# @staticmethod
"""
A static method is a method that doesn't get self.

The code belongs to a class but doesn’t use the object itself.
It eases the readability of the code: when we use @staticmethod, we know that the method does not depend on the state 
of the object itself.
It bounds a method to the class definition.
"""


class MyClass:
    @staticmethod
    def add(a, b):
        return a + b


print(MyClass.add(3, 6))

# @classmethod
"""
Class methods are methods that are not bound to an object but to a class. Its first argument is the class itself 
(remember that classes are objects too).
"""


class MyClass:
    __counter = 0

    @classmethod
    def add(cls, a):
        return cls.__counter + a


my_class_add = MyClass.add(3)
print(my_class_add)
# >> 3

new_class = MyClass()
new_class.__counter = 1

print(new_class.add(3))

"""
@property

Methods used in Object-Oriented Programming (OOPS) which helps to access the private attributes from a class.
"""


class MyClass:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property  # Getter
    def email(self):
        return "{}.{}@gmail.com".format(self.__first_name, self.__last_name)

    @email.setter  # Setter
    def email(self, name):
        self.__first_name = name


newClass = MyClass("John", "Doe")

# print(newClass.email())
# >> TypeError: 'str' object is not callable

print(newClass.email)
newClass.email = 'Sarah'
print(newClass.email)

"""
Example
"""


class Person:
    used_names = set()

    def __init__(self, name, age):
        if name in Person.used_names:
            name = input("That name is taken. Enter another name: ")

        self.name = name
        self.age = age
        self.used_names.add(name)

    @classmethod
    def fromYear(cls, name, birth_year):
        THIS_YEAR = 2020
        return cls(name, THIS_YEAR - birth_year)

    @property
    def professional_name(self):
        return "Mr " + self.name


bob = Person('bob', 32)
bob2 = Person('bob', 38)

print(bob.name)
print(bob2.name)

"""
Analyze the code below. What will be the ouput ?
"""


class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = val
        MyClass.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count


object_1 = MyClass(10)
print("\nValue of object : %s" % object_1.get_val())  # ==> 10
print(MyClass.get_count())  # ==> 1

object_2 = MyClass(20)
print("\nValue of object : %s" % object_2.get_val())  # ==> 20
print(MyClass.get_count())  # ==> 2

"""
Analyze the code below. What will be the ouput ?
"""


class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        MyClass.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            print("Entered value is not an INT, value set to 0")
            return 0
        else:
            return value


a = MyClass(5)
b = MyClass(10)
c = MyClass(15)

print(a.val)  # ==> 5
print(b.val)  # ==> 10
print(c.val)  # ==> 15
print(a.filterint(100))  # ==> 100

"""
Dunder Methods
"""

"""
The __call__ Method
One of the essential unique methods will be used when you try to call the object (meaning adding () at the end of the name: my_object()).
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self):
        print('Person: {}, Age: {}'.format(self.name, self.age))

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return str(self.age)


person1 = Person("Sarah", 25)
person1()
print(len(person1))
print(str(person1))

"""
__repr__ And __str__

Most classes should at least have these unique methods:

object.__str__:
Called by the str() built-in function and by the print function to compute the informal string representation of an object.
__str__ will always be a string representation,



object.__repr__:
Called by the repr() built-in function to compute the official string representation of an object.
__repr__ can be a more “behind the scenes” look at the object.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.age})"


newPerson = Person('Sarah', 24)

print(newPerson)
# >> Person : Sarah 24


"""
Overloading / Overrriding Dunder Method
"""

 #To overload a dunder method, we need to implement it in a class.

class Person:
  def __init__(self, name, lastName):
      self.name = name
      self.lastName = lastName


#Here we overloaded the method by redefining '__repr__ 'using 'def' and passed the argument '(self)'

 def __repr__(self):

# We can write whatever we want inside this method, but we have to return an object.

      return f"{self.__class__.__name__} : {self.name} {self.lastName}"

  def __add__(self,other):
      name = self.name[0] + other.name[1:]
      lastname = other.lastName
      return Person(name,lastname)


father = Person('John', 'Snow')
mother = Person('Kaleesi', 'MotherOfDragons')
# using the __add__() method
dragonChild = father + mother

print(dragonChild)
# >>Person : Jaleesi MotherOfDragons