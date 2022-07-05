# For Loops
students = [
    'Joeri',
    'Ally',
    'Shivastav',
    'Kadeer',
    'Laurent',
    'Bruno',
    'Angkush'
]

for student in students:
    print(student)

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in 'helloworld':
    print(i)

for i in (1, 2, 3):
    print(i)

user_input = int(input('Provide an number: '))
for i in range(0, 13):
    print(user_input * i)

# While Loop
flag = True
while flag:
    num = int(input('Please enter a positive number: '))

    if num > 0:
        flag = False
        print('Congratulations!')
    else:
        print('Number is not positive')

count = 0
while count < 5:
    print(count)
    count += 1

# Break
while True:
    num = int(input('Please provide a positive number:'))

    if num > 0:
        break
    else:
        print('Number is not positive')

# Continue
count = 0
while count < 11:
    count += 1
    if count == 3:
        continue
    else:
        print(count)

print('finished loop')

# Advanced Loops.
# For Loop with Steps: range(start, stop, step)
for num in range(1, 20, 2):
    print(num)

print(list(range(1, 20, 2)))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in alphabet:
    print(char)

for idx in range(len(alphabet)):
    print(idx, alphabet[idx])

for item in enumerate(alphabet):
    print(item)  # tuple

for idx, val in enumerate(alphabet):
    print(idx, val)

# Zip
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

for item in zip(list1, list2, list3):
    print(item)  # returns tuple containing item at the same index from each data set.

# For-Else - Else is optional and is executed once after the for loop. Except on break it will not run.
for num in range(1, 20, 2):
    print(num)
    if num == 11:
        break
else:
    print('Odd numbers generated') # does not run because of break


# While-Else
x = 0
while x < 10:
    print(x)
    x += 1
    if x == 5:
        break
else:
    print(f'x is not smaller than 10. x is {x}.') # does not run because of break.
print('While loop completed')
