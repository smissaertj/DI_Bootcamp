"""
Exercise 1 : What Are You Learning ?
Instructions
Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
Call the function, and make sure the message displays correctly.
"""
import random


def display_message():
    print('I\'m learning about functions')

display_message()

"""
Exercise 2: What’s Your Favorite Book ?
Instructions
Write a function called favorite_book() that accepts one parameter called title.
The function should print a message, such as "One of my favorite books is <title>".
For example: “One of my favorite books is Alice in Wonderland”
Call the function, make sure to include a book title as an argument when calling the function.
"""

def favorite_book(title):
    print(f'One of my favorite books is {title}')

favorite_book('A Brief History of Time')

"""
Exercise 3 : Some Geography
Instructions
Write a function called describe_city() that accepts the name of a city and its country as parameters.
The function should print a simple sentence, such as "<city> is in <country>".
For example “Reykjavik is in Iceland”
Give the country parameter a default value.
Call your function.
"""

def describe_city(city_name, country):
    print(f'{city_name} is located in {country}')

describe_city('Reykjavik', 'Iceland')


"""
Exercise 4 : Random
Instructions
Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
"""
def random_compare(user_number):
    random_int = random.randint(1, 100)
    if user_number == random_int:
        print('Same number')
    else:
        print(f'{user_number} does not equal {random_int}')

random_compare(5)



"""
Exercise 5 : Let’s Create Some Personalized Shirts !
Instructions
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
Call the function make_shirt().

Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
Make a large shirt with the default message
Make medium shirt with the default message
Make a shirt of any size with a different message.

Bonus: Call the function make_shirt() using keyword arguments.
"""

def make_shirt(size='L', print_text='I <3 Python'):
    print(f'The size of the shirt is {size} and the text is:\n{print_text}')

make_shirt()
make_shirt('M')
make_shirt('S', 'This is a small shirt')
make_shirt(size='XL', print_text='This is an XL shirt')


"""
Exercise 6 : Magicians …
Instructions
Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
Call the function make_great().
Call the function show_magicians() to see that the list has actually been modified.
"""

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_list):
    for magician in magician_list:
        print(magician)

def make_great():
    for index in range(0, len(magician_names)):
        magician_names[index] += ' the Great'

make_great()
show_magicians(magician_names)