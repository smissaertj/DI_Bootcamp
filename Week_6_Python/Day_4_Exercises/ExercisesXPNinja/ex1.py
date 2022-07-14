"""
Exercise 1: Formula
Instructions
Write a program that calculates and prints a value according to this given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
For example, if the user inputs: 100,150,180
The output should be:

18,22,24
"""
import math


def calculate(*args):
    C = 50
    H = 30

    result = [[round(math.sqrt((2 * C * arg) / H)) for arg in args]]
    result = [str(i) for i in result]
    print(','.join(result))


calculate(100, 150, 180)
