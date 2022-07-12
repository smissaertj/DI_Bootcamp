"""
The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, select only the alpha characters and connect them, then he replaces every group of symbols between two alpha characters by a space.

Using his technique, try to decode this matrix:
    7i3
    Tsi
    h%x
    i #
    sM
    $a
    #t%
    ^r!
"""
import re

matrix = [
    '7i3',
    'Tsi',
    'h%x',
    'i #',
    'sM ',
    '$a ',
    '#t%',
    '^r!'
]

decoded = ''
for el in zip(*matrix):
    for char in el:
        if re.match('[a-zA-Z\s]', char):
            decoded += char
print(decoded)