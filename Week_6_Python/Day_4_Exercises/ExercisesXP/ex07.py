"""
Ask the user to input their favorite fruit(s) (one or several fruits).
Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
Store the favorite fruit(s) in a list (convert the string of words into a list of words).
Now that we have a list of fruits, ask the user to input a name of any fruit.
If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
"""

fav_fruits = input('Provide a space separated list of your favourite fruits: ').split(' ')
fruit = input('Name any fruit: ')

if fruit in fav_fruits:
    print('You chose one of your favorite fruits! Enjoy')
else:
    print('You chose a new fruit. I hope you enjoy!')
