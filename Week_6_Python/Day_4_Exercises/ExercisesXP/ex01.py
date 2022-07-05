my_fav_numbers = {1, 3, 6, 12, 24}
my_fav_numbers.add(36)
my_fav_numbers.add(48)
my_fav_numbers.pop()
print(my_fav_numbers)

friend_fav_numbers = {2, 4, 7, 13, 25}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)