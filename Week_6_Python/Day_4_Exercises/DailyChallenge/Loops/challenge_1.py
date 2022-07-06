number = int(input('Provide a number: '))
length = int(input('Provide length: '))
result = []

for i in range(1, length + 1):
    result.append(i * number)
else:
    print(result)