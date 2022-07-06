"""
Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
Sort the list in alphabetical order.
Return “Nothing” if you can’t afford anything from the store.

The key is the product, the value is the price

items_purchase = {
  "Water": "1",
  "Bread": "3",
  "TV": "1,000",
  "Fertilizer": "20"
}

wallet = "300"

➞ ["Bread", "Fertilizer", "Water"]

items_purchase = {
  "Apple": "4",
  "Honey": "3",
  "Fan": "14",
  "Bananas": "4",
  "Pan": "100",
  "Spoon": "2"
}

wallet = "100"

➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

items_purchase = {
  "Phone": "999",
  "Speakers": "300",
  "Laptop": "5,000",
  "PC": "1200"
}

wallet = "1"

➞ "Nothing"
"""

items_purchase = {
  "Water": "1",
  "Bread": "3",
  "TV": "1000",
  "Fertilizer": "20"
}

wallet = "300"

affordable_items = []
for k, v in items_purchase.items():
    if int(v) <= int(wallet):
        affordable_items.append(k)
else:
    print(sorted(affordable_items))


