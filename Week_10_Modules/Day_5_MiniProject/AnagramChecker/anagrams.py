from anagram_checker import AnagramChecker
from string import ascii_letters

def menu():
    """ Show UI """

    while True:
        print('(I)nput word')
        print('(E)xit')
        user_choice = input('Choose a menu option above: ').lower()

        if user_choice == 'i':
            while True:
                user_input = input('Please enter one word: ')
                invalid_chars = [char for char in user_input if char not in ascii_letters]

                if len(user_input.split(' ')) > 1:
                    # The user provided more than 1 word
                    print('More than one word was provided.')

                if invalid_chars:
                    print('Only input letters. No numbers or special characters')

                else:
                    user_input.strip()
                    result = AnagramChecker()
                    is_valid = result.is_valid_word(user_input)
                    anagrams = result.get_anagrams(user_input)

                    if is_valid:
                        print(f'{user_input} is a valid English word.')
                        print(f'Anagrams for your word: {", ".join(anagrams)}')
                    else:
                        print(f'{user_input} is not a valid English word.')

                    break

        if user_choice == 'e':
            break



if __name__ == '__main__':
    """ Application entrypoint """
    menu()