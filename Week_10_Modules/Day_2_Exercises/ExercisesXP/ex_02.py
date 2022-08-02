import random
def rand_int(i):
    rand_int = random.randint(1, 101)
    if i == rand_int:
        print('Success!')


rand_int(50)