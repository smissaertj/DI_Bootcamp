# Try to create a countdown to your birthday !
#
# For example : "My birthday is in 45 days, and 10:29:46"

import datetime

next_birthday_dt = datetime.datetime.strptime("15/07/2023", "%d/%m/%Y")
now = datetime.datetime.now()
delta_dt = next_birthday_dt - now
days, hours, minutes = delta_dt.days, delta_dt.seconds // 3600, delta_dt.seconds // 60 % 60

print(f"My birthday is in {days} days, {hours} hours and {minutes} minutes.")
