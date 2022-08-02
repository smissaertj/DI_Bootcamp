"""
Exercise 3: Python Password Generator
Instructions
Create a Python program that will generate a good password for you.

Program flow:

Ask the user to type in the number of characters that the password should have (password length) – between 6 and 30 characters.
Validate the input. Make sure the user is inputing a number between 6 to 30. Create a loop which will continue to ask the user for an input until they enter a valid one.

Generate a password with the required length.

Print the password with a user-friendly message which reminds the user to keep the password in a safe place!

Rules for the validity of the password

Each password should contain:
At least 1 digit (0-9)
At least 1 lower-case character (a-z)
At least 1 upper-case character (A-Z)
At least 1 special character (eg. !, @, #, $, %, ^, _, …)
Once there is at least 1 of each, the rest of the password should be composed of more characters from the options presented above.

Create a test function first!

Do the following steps 100 times, with different password lengths:
Generate a password.
Test the password to ensure that:
it fulfills all the requirements above (eg. it has at least one digit, etc.)
it has the specified length.
"""

import random
import string


def generate_password(len_passwd):
    passwd = []
    char_list = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

    for el in char_list:
        passwd.append(random.choice(el))

    character_pool = ''.join(char_list)
    while len(passwd) < len_passwd:
        passwd.append(random.choice(character_pool))

    random.shuffle(passwd)
    print(f"Password: {''.join(passwd)}\nKeep it in a safe place!")


len_passwd = 0
while len_passwd < 6 or len_passwd > 30:
    len_passwd = int(input('Number of characters (6 to 30): '))
else:
    generate_password(len_passwd)
