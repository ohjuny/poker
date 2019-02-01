from card import *
from random import randrange

class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.deck.append(Card(rank, suit))
    
    def shuffle(self):
        for i in range(1000):
            copy = self.deck.copy()
            self.deck.clear()

            # index ranges from 0 to 51 (inclusive) initially
            while copy:
                index = randrange(len(copy))
                self.deck.append(copy[index])
                copy.pop(index)

    def print_deck(self):
        print("Cards in deck:")
        for card in self.deck:
            print("    {}".format(card))
        print()
    
    def get_top(self):
        return self.deck[0]
    
    def remove_top(self):
        self.deck.pop(0)

###

# a = Deck()
# a.print_deck()
# a.shuffle()
# a.print_deck()