"""
Exercise 9 : Faker Module
Instructions
Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
Create an empty list called users. Tip: It should be a list of dictionaries.
Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress,
langage_code. Use faker to populate them with fake data.
"""

import random
from faker import Faker
fake = Faker()

users = []
locales_list = ['en_US', 'de_DE', 'fr_FR']

def add_user(name, address, language_code):
    user = {'name': name, 'address': address, 'language_code': language_code}
    users.append(user)


add_user(fake.name(), fake.address(), random.choice(locales_list))
add_user(fake.name(), fake.address(), random.choice(locales_list))
add_user(fake.name(), fake.address(), random.choice(locales_list))

print(users)