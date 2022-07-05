sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

"""
Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

sandwich_orders.append(sandwich_orders[-1])
sandwich_orders.append(sandwich_orders[-1])
print(sandwich_orders)

print('We ran out of pastrami.')

finished_sandwiches = []
for sandwich in sandwich_orders:
    if sandwich == 'Pastrami sandwich':
        sandwich_orders.remove(sandwich)
    else:
        print(f'Making {sandwich}')
        finished_sandwiches.append(sandwich)
else:
    print(f'Sandwiches that have been made: {", ".join(finished_sandwiches)}')

