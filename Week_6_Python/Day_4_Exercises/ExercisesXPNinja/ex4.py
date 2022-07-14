"""
Exercise 4
Instructions
Write a program that prints the frequency of the words from the input.

Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:

    2:2
    3.:1
    3?:1
    New:1
    Python:5
    Read:1
    and:1
    between:1
    choosing:1
    or:2
    to:1
"""

def word_frequency(string):
    string_list = string.split(' ')
    unique_string = []

    for i in string_list:
        if i not in unique_string:
            unique_string.append(i)

    for i in sorted(unique_string):
        print(f'{i}: {string_list.count(i)}')


word_frequency('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')