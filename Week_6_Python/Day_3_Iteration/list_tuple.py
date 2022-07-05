# Data Types
## Primitive: Integer, String, Boolean, Float
## Non-Primitive: List, Array, File, Tuple, Set

# Sequences - category of data types
## Lists - mutable, can contain other data types
vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
vowel_list = [1, 2, 3, 4, 5]
print(vowel_list)

## Tuple - immutable
vowel_tuple = ('a', 'e', 'i', 'o', 'u', 'y')
print(vowel_tuple)

vowel_tuple = (1, 2, 3, 4, 5,)
print(vowel_tuple[0])
# vowel_tuple[0] = 'a'  ==> TypeError - cannot reassign a value

## Strings - Sequence that can only contain characters
vowel_string = 'aeiouy'

# Sequence indexing starts at position 0
print(vowel_list[0])
print(len(vowel_list))
print(vowel_list[-1])

# Range
print(vowel_list[:3])  # Start at Zero, end at (but don't include) index 3.
print(vowel_string[:3])
print(vowel_list[3:]) # Start at index 3 until end
print(vowel_list[1:3])

# List Methods
vowel_list[0] = 'b'
print(vowel_list)
#vowel_list[10] = 'z'  ==> IndexError: index 10 does not exist.

vowel_list.append('z')
vowel_list.remove('b')
print(vowel_list)

missing_vowel = ['a']
complete_vowels = missing_vowel + vowel_list
print(complete_vowels)


# sorting
unsorted_list = ['z', 'p', 'a', 'o']
print(sorted(unsorted_list))