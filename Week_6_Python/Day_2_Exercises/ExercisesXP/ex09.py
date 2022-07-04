height_inches = int(input('What is your height in Inches: '))
height_cm = height_inches * 2.54

if height_cm > 145:
    print('You\'re tall enough to ride!')
else:
    print('You need to grow a bit more to ride!')
