"""
Part 1 : Quizz :
Answer the following questions

What is a class?
A blueprint for creating objects.

What is an instance?
An object that was instantiated from a class.

What is encapsulation?
The bundling of data and methods, which is exactly what creating a class does.

What is abstraction?
The process of handling complexity by hiding unnecessary information from the user.

What is inheritance?
Acquiring all properties and behaviours of the parent object.


What is multiple inheritance?
Acquiring properties and behaviours of multiple parent objects.


What is polymorphism?
The fact that one task can be accomplished in multiple ways.

What is method resolution order or MRO?
In multi-inheritance, the method resolution order defines the search path for the right methods in parent classes.
"""

"""
Part 2: Create A Deck Of Cards Class.
The Deck of cards class should NOT inherit from a Card class.

The requirements are as follows:

The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
The Deck class :
should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
"""

import random

class Card():
    def __init__(self):
        self.suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Deck(Card):
    def __init__(self):
        super().__init__()
        self.cards = []

    def shuffle(self):
        for suit in self.suit:
            for value in self.value:
                self.cards.append([suit, value])
        random.shuffle(self.cards)

    def deal(self):
        card = self.cards[0]
        self.cards.remove(card)
        print(f'Card: {card[1]} of {card[0]}')


my_deck = Deck()
my_deck.shuffle()
my_deck.deal()
my_deck.deal()
my_deck.deal()
my_deck.deal()