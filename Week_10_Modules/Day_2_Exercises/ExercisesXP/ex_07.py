"""
Exercise 7 : Upcoming Holiday
Instructions
Write a function that displays today’s date.
The function should also display the amount of time left from now until the next upcoming holiday and print which
 holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
Hint: Start by hardcoding the datetime and name of the upcoming holiday.
"""
import datetime

upcoming_date = {'holiday': {'name': 'Assumption of Mary', 'date': '15/08/2022'}}

def today(upcoming_date):
    now = datetime.datetime.now()
    upcoming_date_name = upcoming_date['holiday']['name']
    upcoming_date = upcoming_date['holiday']['date']
    upcoming_date_obj = datetime.datetime.strptime(upcoming_date, '%d/%m/%Y')
    timedelta_obj = upcoming_date_obj - now
    days, hours, minutes = timedelta_obj.days, timedelta_obj.seconds // 3600, timedelta_obj.seconds // 60 % 60
    seconds = timedelta_obj.seconds - (hours*3600 + minutes*60)
    print(f'The next holiday, {upcoming_date_name}, is in {days} days and {hours}:{minutes}:{seconds} hours.')


today(upcoming_date)