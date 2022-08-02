import string
import random

def random_string():
    my_str = ''
    while len(my_str) < 5:
        my_str += random.choice(string.ascii_letters)
    print(my_str)


random_string()