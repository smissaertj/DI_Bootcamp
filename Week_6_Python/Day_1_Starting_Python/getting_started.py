print('hello world')
print(5 + 5)
print((5).__add__(5))
print('damien'.title())
print(5 / 4)
print(5 // 4)  # Floor division
print(5 % 4)
print(type('1'))
print(type(1))
print(type(False))
print(type('False'))
print(type(1.25))

print('hello world'.capitalize())

print('Variables and Conditionals')
name = 'laurent'
age = 34

print('My name is ' + name + ' and my age is ' + str(age))
print('My name is {} and my age is {}'.format(name, age))
print('My name is', name, 'and my age is', age)
print(f'My name is {name} and my age is {age}')


name = input('Please state your name: ')
age = input('Please state your age: ')
new_age = int(age) + 5
print(f'My name is {name} and my age is {new_age}.')


if int(age) > 18:
    print('You\'re an adult')
print('Congratulations!')

if int(age) > 60:
    print('You can travel for free.')
elif int(age) == 60:
    print('You can now travel free')
elif int(age) == 59:
    print('You have to wait one more year')
else:
    print('You need to pay')
print('finished')

a = 1
b = 2
c = 0

if (a < b) and (c > a):
    print('Both conditions evaluate to True')
    print('c is greater than a')
elif a < b or c > a:
    print('One condition evaluates to True')
else:
    print('All conditions evaluate to False')


vowels = "aeiouy"
letter = 'a'
print(letter in vowels)

hobbies = ['tv', 'eating', 'coding', 'gaming']
student_hobby = 'coding'
if student_hobby in hobbies:
    print('welcome to the club')
