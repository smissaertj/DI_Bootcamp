"""
Exercise 2 : List Of Integers
Instructions
Given a list of 10 integers to analyze. For example:

    [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
    [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
    [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
    [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
Store the list of numbers in a variable.
Print the following information:
a. The list of numbers – printed in a single line
b. The list of numbers – sorted in descending order (largest to smallest)
c. The sum of all the numbers
A list containing the first and the last numbers.
A list of all the numbers greater than 50.
A list of all the numbers smaller than 10.
A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
The numbers without any duplicates – also print how many numbers are in the new list.
The average of all the numbers.
The largest number.
10.The smallest number.
11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
12.Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
13.Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
14.Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
15.Bonus: Will the code work when the number of random numbers is not equal to 10?
"""

numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7, 3, 5, 7, 99, 0, 0]

print(numbers)
print(sorted(numbers, reverse=True))
print(sum(numbers))
print([numbers[0], numbers[-1]])
print(list(filter(lambda i: (i > 50), numbers)))
print(list(filter(lambda i: (i < 10), numbers)))
print(list(map(lambda i: i**2, numbers)))
no_duplicates_list = list(set(numbers))
print(f'{no_duplicates_list} - length: {len(no_duplicates_list)}')
print(sum(numbers) / len(numbers))
print(max(numbers))
print(min(numbers))
