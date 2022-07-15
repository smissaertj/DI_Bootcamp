"""
Exercise 1 : Box Of Stars
Instructions
Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
"""

def box_printer(*strings):
    string_lengths = []

    for i in strings:
        string_lengths.append(len(i))

    box_width = max(string_lengths) + 4
    box_height = len(list(strings)) + 2

    print('*' * box_width)
    for string in strings:
        spaces_num = (box_width - 4) - len(string)
        print('* ' + string + ' ' * spaces_num + ' *')
    print('*' * box_width)


box_printer("Hello", "World", "in", "reallylongword", "a", "frame")