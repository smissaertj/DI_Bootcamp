sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

"""
Use the above list called sandwich_orders.
Make an empty list called finished_sandwiches.
As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.
"""

finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f'Making {sandwich}')
    finished_sandwiches.append(sandwich)
else:
    print(f'Sandwiches that have been made: {", ".join(finished_sandwiches)}')