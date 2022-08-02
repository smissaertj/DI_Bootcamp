"""
Instructions :
Consider this list

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
Look at this result :
{"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
You have to recreate the result using a translator module.
"""


# https://pypi.org/project/translate/
from translate import Translator


from_lang = 'fr'
to_lang = 'en'
translator = Translator(from_lang=from_lang, to_lang=to_lang)

def translate(word_list):
    translation = {}

    for word in word_list:
        translation[word] = translator.translate(word)

    print(translation)


translate(["Bonjour", "Au revoir", "Bienvenue", "A bientôt"])