# Map example
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
print(f"fruits before the change {fruit}")
new_fruits = list(map(lambda s: s.upper(), fruit))
print(f"fruits after the change {new_fruits}")

# Filter example
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
fruits_starts_with_a = list(filter(lambda s: s[0] == "A", fruit))
print(f"Fruits start with A are: {fruits_starts_with_a}")

# Lambda example
my_function = lambda s: s.upper()
# This is the same as doing:
def my_function(s):
    return s.upper()


# Reduce example
from functools import reduce
numbers = [1, 3, 5, 7]  # [4, 5, 7] ==> [9, 7] ==> [16]
sum_of_numbers = reduce(lambda first, second: first + second, numbers)
print(sum_of_numbers)


# Exercise
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# def is_4_letters_or_less(s):
#     return len(s) <= 4

result = list(filter(lambda name: len(name) <= 4, people))
print(result)

hello = list(map(lambda name: f'Hello {name}', result))
print(hello)


