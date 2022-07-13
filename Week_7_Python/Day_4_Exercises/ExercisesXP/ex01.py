import random


def get_random_temp(season):
    temp = ()

    if season == 'winter':
        temp = (-10, 0)
    elif season == 'fall':
        temp = (0, 16)
    elif season == 'spring':
        temp = (16, 23)
    elif season == 'summer':
        temp = (24, 32)

    return random.randint(*temp)


def main():
    season = input('Season? ')
    temp = get_random_temp(season)
    print(f'The temperature is {temp} degrees Celsius.')

    if temp < 0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif 0 <= temp < 16:
        print('Quite chilly! Don’t forget your coat')
    elif 16 <= temp < 23:
        print('It\'s a cool day today!')
    elif 23 <= temp < 32:
        print('It\'s a hot day today!')
    else:
        print('Take care, seems like there might be a heat wave!')


main()
