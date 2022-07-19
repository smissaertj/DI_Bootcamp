"""
# Object Oriented Programming

Object-oriented Programming, or OOP for short, mean structuring programs so that properties and behaviors are bundled
into individual objects.

An object could represent a person with a name, property, age, address, etc., with behaviors like walking, talking,
breathing, and running. Or an email with properties like recipient list, subject, body, etc., and behaviors like
adding attachments and sending.

Object-oriented programming is an approach for modeling concrete, real-world things like cars and relations between
things like companies and employees, students and teachers, etc. OOP models real-world entities as software objects,
which have some data associated with them and can perform certain functions.


# Classes
Each thing or object is an instance of some class.

Classes are used to create new user-defined data structures that contain arbitrary information about something. In
the case of an animal, we could create an Animal class to track properties about the Animal such as its name and age.

It’s important to note that a class provides structure—it’s a blueprint for how something should be defined,
but it doesn't offer any actual content itself. The Animal class may specify that the name and age are necessary for
determining an animal, but it will not state what a specific animal’s name or age is. It may help to think of a class
as an idea for how something should be defined.

# Objects (Instances) While the class is the blueprint, an instance is a copy of the class with actual values,
literally an object belonging to a specific class. It’s not an idea anymore; it’s a real animal, like a dog named
Roger eight years old.
"""


# Defining a Class
class Dog():
    pass


# Creating an object (instance of a class):
class Dog():
    pass


shelter_dog = Dog()

# Attributes
# Attributes are like variables; they can be any data type, the only difference is that they belong to an object.
class Dog():
    pass

shelter_dog = Dog()
shelter_dog.color = 'Brown'


# The __init__ Method
"""When an object is created, python automatically runs the __init__() method of the class. This method must have at 
least one argument, self (it doesn’t have to be called self, but a python convention). self refers to the object 
itself. Although this function receives one argument (self), we don’t need to pass it, it will be passed 
automatically by python as the first argument.
You can add arguments to __init__. Those arguments would be passed on the object creation (shelter_dog = Dog()).
"""

class Dog():
    # Initialize instance attributes
    def __init__(self, name_of_dog):
        print('A new Dog has been initialized!')
        print('His name is', name_of_dog)
        self.name = name_of_dog


shelter_dog = Dog('Rex')
print(shelter_dog.name)


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


first_person = Person('John', 36)
print(first_person.name, first_person.age)


# Instance Methods
"""Instance methods are defined inside a class and are used to describe a function that belongs to a class. For 
example, in real life, the “bark” function belongs to “Dog” class. 

Instance methods can be used to perform operations with the attributes, get the contents of an instance, 
and many other things. 

To define a method, use the def keyword inside the class, like we were doing with the __init__ method. All instance 
methods need to receive self as the first argument; this allows us to play with the object inside the method. """

class Dog():
    # Initialize instance attributes
    def __init__(self, name_of_dog):
        print('A new Dog has been initialized!')
        print('His name is', name_of_dog)
        self.name = name_of_dog

    def bark(self):
        print(f'{self.name} barks! WAF!')

    def walk(self, number_of_meters):
        print(f'{self.name} walked {number_of_meters} meters.')

    def rename(self, new_name):
        self.name = new_name

shelter_dog = Dog('Rex')
shelter_dog.bark()
shelter_dog.walk(10)
shelter_dog.rename('Paul')
print(shelter_dog.name)


# Example code
class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)
