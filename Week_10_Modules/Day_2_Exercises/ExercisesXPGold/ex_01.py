"""
Exercise 1 : Regular Expression #1
Instructions
Hint: Use the RegEx (module)

Use the regular expression module to extract numbers from a string.

Example

return_numbers('k5k3q2g5z6x9bn')
// Excepted output : 532569
"""

import re

def return_numbers(string):
    print(''.join(re.findall('\d', string)))

return_numbers('k5k3q2g5z6x9bn')
#Excepted output : 532569