# r	Opens a file for reading. (default)
# w	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# x	Opens a file for exclusive creation. If the file already exists, the operation fails.
# a	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# t	Opens in text mode. (default)
# b	Opens in binary mode.
# +	Opens a file for updating (reading and writing)


f = open('secrets.txt', mode='w')
f.write("This is top secret.\n")
f.close()

with open('My_Secret.txt', mode='w+') as f:
    f.write('This is the first line.\n')
    f.write('File will automatically be closed.\n')



# Read the file line by line
with open('nameslist.txt', mode='r') as f:
    content = f.readlines()
    # print(content)

# Read only the 5th line of the file
with open('nameslist.txt', mode='r') as f:
    content = f.readlines()[4:5]
    # print(content)

# Read only the 5 first characters of the file
with open('nameslist.txt', mode='r') as f:
    print(f.read(5))


# Read all the file and return it as a list of strings. Then split each word
with open('nameslist.txt', mode='r') as f:
    content = f.readlines()
    lines = list(map(lambda line: line.strip(), content))
    print(lines)

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
with open('nameslist.txt', mode='r') as f:
    count = {'Darth': 0, 'Luke': 0, 'Lea': 0}
    content = f.readlines()

    for name in content:
        for key in count.keys():
            if name.strip() == key:
                count[key] += 1
    else:
        print(count)

    # print(content.count('Darth')


# Append your first name at the end of the file
with open('nameslist.txt', mode='a+') as f:
    f.write('Joeri\n')


# Append "SkyWalker" next to each first name "Luke"
lines = []
with open('nameslist.txt') as f:
    content = f.readlines()
    lines = list(map(lambda line: line.strip(), content))


with open('nameslist.txt', 'w') as f:
    for name in lines:
        if name == 'Luke':
            name += " Skywalker"
        f.write(name + '\n')

try:
    with open('nonexistingfile.txt', mode='r') as f:
        print(f.read())
except FileNotFoundError as err:
    print('File does not exist')
except IOError as err:
    print('IO Error')
    raise err