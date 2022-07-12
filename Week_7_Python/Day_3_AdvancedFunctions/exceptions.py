valid_input = False

while not valid_input:  # it's the same like valid_input == False
    try:
        num1 = int(input("please enter the first parameter: "))
        num2 = int(input("please enter the second parameter: "))
        print(f"the result of the division is {num1 / num2}")
    except ZeroDivisionError:
        # this code will be running if we get and exception of type ZeroDivisionError
        print("can't divide by zero")
    except ValueError:
        # this code will be running if we get an exception of type ValueError
        print("please enter an integer")
    else:
        # this code will be running if there is no exceptions
        valid_input = True
    finally:
        # this code always will be running
        print("all of the code inside the finally will always run")

print("Good bye")

import random
from time import sleep


def get_current_temperature():
    return random.randint(0, 100)


def main():
    while True:
        current_temperature = get_current_temperature()

        if current_temperature < 5:
            # Create a custom Exception
            raise Exception(f'The current temperature {current_temperature} is too low.')

        print(f'The current temperature is {current_temperature}')
        sleep(2)

main()
