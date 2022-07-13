def divide_by_zero(x):
    try:
        print(x / 0)
    except ZeroDivisionError:
        print('You cannot divide by zero.')


divide_by_zero(5)