# my_list = [param for param in iterable]
my_list = [char for char in 'helloooo']
#print(my_list)

my_list2 = [num for num in range(0, 100)]
#print(my_list2)

my_list3 = [num*2 for num in range(0, 100)]
#print(my_list3)

my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]
#print(my_list4)


some_list = ['a', 'b', 'c', 'd', 'b', 'c', 'd', 'e', 'e']
duplicates = list(set([char for char in some_list if some_list.count(char) > 1]))
print(duplicates)