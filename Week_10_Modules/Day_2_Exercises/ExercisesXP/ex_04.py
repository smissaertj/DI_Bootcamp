"""
Exercise 4 : Current Date
Instructions
Create a function that displays the current date.
Hint : Use the datetime module.
"""

import datetime

def current_date():
    print(datetime.datetime.now().date())


current_date()