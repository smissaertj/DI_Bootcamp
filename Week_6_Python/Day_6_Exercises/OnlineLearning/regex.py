import re

string = 'search this inside of this text please'
print('search' in string)

pattern = re.compile('this')
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.match(string)

pattern = re.compile('search this inside of this text please')
d = pattern.fullmatch(string)


print(a.group())
print(b)
print(c)
print(d)