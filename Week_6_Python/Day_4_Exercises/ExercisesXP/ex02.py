my_tuple = (1, 2, 3, 4, 5)
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# my_tuple[0] = 2222  ==> TypeError

# However, we can concatenate a new tuple to the existing tuple
my_tuple += ('a', 'b')
print(my_tuple)

# But not any other data type
my_tuple += ['c', 'd']
my_tuple += 'e'
my_tuple += {'f', 'g'}
