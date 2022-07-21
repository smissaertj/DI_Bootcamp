"""
Exercise 1 : Family
Instructions
Create a class called Family and implement the following attributes:

members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
last_name : (string)

Initial members data:

[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]
Implement the following methods:

born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
family_presentation: a method that prints the family’s last name and all the members’ first name.
"""

members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]


class Family():
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        print('Congratulations!')
        self.members.append(dict(kwargs))

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return True if member['age'] > 18 else False

    def family_presentation(self):
        first_names = ', '.join([member['name'] for member in self.members])
        print(f'{self.last_name}: {first_names}')


my_family = Family(members, 'Smissaert')
my_family.born(name='Joeri', age=15, gender='Male', is_child=True)

print(my_family.is_18('Sarah'))
print(my_family.is_18('Joeri'))
my_family.family_presentation()