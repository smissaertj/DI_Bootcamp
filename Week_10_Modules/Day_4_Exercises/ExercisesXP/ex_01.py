import random

def get_words_from_file():
    with open('sowpods.txt', mode='r') as file:
        content = file.readlines()
        return content


def get_random_sentence(length):
    random_words = []
    while len(random_words) < length:
        random_words.append(random.choice(get_words_from_file()).strip())
    return ' '.join(random_words).lower()


def main():
    print('Description:\n')

    try:
        sentence_length = int(input('Number of words? '))

        while True:
            if sentence_length >= 2 and sentence_length <= 20:
                sentence = get_random_sentence(sentence_length)
                print(sentence)
                break
            else:
                raise ValueError
    except ValueError as err:
        print(f'{err}\nAcceptable values: integer between 2 and 20.')


main()