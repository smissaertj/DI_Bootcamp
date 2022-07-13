from datetime import datetime


def get_age(year, month, day):
    current_date = datetime.now()
    birthday = datetime.strptime(f'{year} {month} {day}', '%Y %m %d')
    return round((current_date - birthday).days / 365)


def can_retire():
    gender = input('Gender? (male, female) ')
    date_of_birth = input('Birthday? (yyyy/mm/dd) ').split('/')
    age = get_age(*date_of_birth)
    return bool(age >= 60)


if can_retire():
    print(f'You have reached retirement age.')
else:
    print(f'You have not yet reached retirement age.')
