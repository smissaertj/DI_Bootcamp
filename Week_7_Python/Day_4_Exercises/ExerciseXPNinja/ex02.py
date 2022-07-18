"""
Exercise 2 : From English To Morse
Instructions
Write a function that converts English text to morse code and another one that does the opposite.
Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.
"""

morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    1: '.----', 2: '..---', 3: '...--', 4: '....-', 5: '.....', 6: '-....', 7: '--...', 8: '---..', 9: '----.',
    0: '-----', ',': '--..--', '?': '..--..', ':': '---...', '-': '-....-', '"': '.-..-.', '(': '-.--.', '=': '-...-',
    '*': '-..-', '.': '.-.-.-', ';': '-.-.-.', '/': '-..-.', "'": '.----.', '_': '..--.-', ')': '-.--.-', '+': '.-.-.',
    '@': '.--.-.'
}


def eng_to_morse(string):
    word_list = string.split(' ')
    encoded_letters = []
    
    for word in word_list:
        for char in word:
            encoded_letters.append(morse_code[char.lower()])
        encoded_letters.append(' ') # Add a space between each word.

    return ' '.join(encoded_letters)


def morse_to_eng(string):
    morse_list = string.split(' ')
    print(morse_list)

    decoded_letters = []
    for letter in morse_list:
        if letter == '':
            decoded_letters.append(' ')
        for k, v in morse_code.items():
            if v == letter:
                decoded_letters.append(k)

    return ''.join(decoded_letters)


print(eng_to_morse('Sending out an SOS'))
print(morse_to_eng(eng_to_morse('Sending out an SOS')))
