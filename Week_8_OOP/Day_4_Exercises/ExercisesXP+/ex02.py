"""
Exercise 2 : TheIncredibles Family
Instructions
Create a class called TheIncredibles. This class should inherit from the Family class:

This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
Initial members data:

[
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]


2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old.
 If not raise an exception (look up exceptions) which stated they are not over 18 years old.


3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name
(ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.


4. Call the incredible_presentation method.
5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
6. Call the incredible_presentation method again.
"""

members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
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
        first_names = [member['name'] for member in self.members]
        print(f'{self.last_name}: {", ".join(first_names)}')


class TheIncredibles(Family):
    def use_power(self, name):
        if self.is_18(name):
            print(''.join([member['power'] for member in self.members if member['name'] == name]))
        else:
            raise Exception('Member is not over 18 years old.')

    def incredible_presentation(self):
        super().family_presentation()
        powers = ', '.join([member['power'] for member in self.members])
        print(f'Powers: {powers}')



test = TheIncredibles(members, 'test_last_name')
test.use_power('Sarah')
test.incredible_presentation()
test.born(name='Jack', age=1, gender='Male', is_child=True, power='Unknown power')
test.incredible_presentation()