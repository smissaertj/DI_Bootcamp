"""
Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
"""

topping = ''
topping_list = []
while topping == '' or topping != 'quit':
    topping = input('Provide a pizza topping: ')
    if topping != 'quit':
        topping_list.append(topping)
else:
    print(f'Toppings: {" ".join(topping_list)}')
    print(f'Total Price: {10 + (len(topping_list) * 2.5)}')
