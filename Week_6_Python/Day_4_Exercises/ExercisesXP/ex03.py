basket = ["Banana", "Apples", "Oranges", "Blueberries"];

"""
Remove “Banana” from the list.
Remove “Blueberries” from the list.
Add “Kiwi” to the end of the list.
Add “Apples” to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)
"""

basket.remove('Banana')
basket.remove('Blueberries')
basket.append('Kiwi')
basket.insert(0, 'Apples')
print(basket.count('Apples'))
basket.clear()
print(basket)