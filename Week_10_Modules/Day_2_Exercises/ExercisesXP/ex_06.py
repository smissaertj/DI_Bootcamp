"""
Exercise 6 : Birthday And Minutes
Instructions
Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message
stating how many minutes the user lived in his life.
"""

import datetime

def minutes_alive(date):
    date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
    now = datetime.datetime.now()
    timedelta_obj = now - date_obj
    minutes = round(timedelta_obj.total_seconds() / 60, 2)
    print(f'You\'ve been alive for {minutes} minutes.')

minutes_alive('15/07/1986')