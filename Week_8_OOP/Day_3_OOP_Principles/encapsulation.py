# Encapsulation
"""
We can restrict access to methods and variables. This prevents data from direct modification, which is called
encapsulation. In Python, we denote private attributes using underscore as prefix i.e., single _ or double __.

Let's define an object class Computer and try to access its variables and methods both private and global.
"""


class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price


c = Computer()
#c.sell()
# c.__sell() ==> AttributeError

c.__max_price = 1000
c.sell() # The price did not change
c.set_max_price(1000)
c.sell()