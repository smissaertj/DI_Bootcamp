"""
Exercise 1: Cats
Instructions
Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

Instantiate three Cat objects using the code provided above.
Outside of the class, create a function that finds the oldest cat and returns the cat.
Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
"""
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


def oldest_cat(*args):
        cats = {}
        for arg in args:
            cats[arg.name] = arg.age

        cat_tuples = sorted(cats.items(), key=lambda item: item[1], reverse=True)
        oldest_cat = cat_tuples[0]
        print(f'The oldest cat is {oldest_cat[0]}, and is {oldest_cat[1]} years old.')


cat1 = Cat('Joe', 1)
cat2 = Cat('John', 2)
cat3 = Cat('Jake', 3)

oldest_cat(cat1, cat2, cat3)