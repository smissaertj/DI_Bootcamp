"""
Exercise 2 : Regular Expression #2
Instructions
Hint: Use the RegEx (module)

Ask the user for their full name (example: “John Doe”), and check the validity of their answer:
The name should contain only letters.
The name should contain only one space.
The first letter of each name should be upper cased.
"""
import re

def validate_name(full_name):
    if re.search('\d', full_name):
        print('Name can only contain letters.')

    if len(re.findall('\s', full_name)) > 1:
         print('Name can only contain 1 space.')

    for i in re.split('\s', full_name):
        if i[0].islower():
            print(f'{i} should start with a capital letter.')


full_name = input('Full name? ')
validate_name(full_name)