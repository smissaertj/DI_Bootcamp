import random

input_string = input('Provide a string of exactly 10 characters long: ')

if len(input_string) < 10:
    print('String not long enough')
elif len(input_string) > 10:
    print('String too long')
else:
    print(f'First character: {input_string[0]}')
    print(f'Last character: {input_string[-1]}')

    new_string = ''
    for char in input_string:
        new_string += char
        print(new_string)

    shuffled_string = list(input_string)
    random.shuffle(shuffled_string)

    print(''.join(shuffled_string).strip())
