"""
Exercise 5 : Amount Of Time Left Until January 1st
Instructions
Create a function that displays the amount of time left from now until January 1st.
(Example: the 1st of January is in 10 days and 10:34:01hours).
"""

import datetime

def time_left(future_date):
    now = datetime.datetime.now()
    future_date_dt = datetime.datetime.strptime(future_date, '%d/%m/%Y')
    time_delta = future_date_dt - now
    days, hours, minutes = time_delta.days, time_delta.seconds // 3600, time_delta.seconds // 60 %60
    print(f'{future_date} is in {days} days, {hours} hours and {minutes} minutes.')


time_left('01/01/2023')