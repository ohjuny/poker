from card import *

class Player:
    def __init__(self, name, bank=0):
        self.name = name
        self.bank = bank
        self.hand = []
        self.score = 0 # used to store how "good" hand is (after game)

    def add_to_hand(self, card):
        self.hand.append(card)

    def get_name(self):
        return self.name

    def get_bank(self):
        return self.bank

    def get_hand(self):
        return self.hand

    def get_score(self):
        return self.score
    
    def set_score(self, score):
        self.score = score

    def set_bank(self, bank):
        self.bank = bank

    def print_hand(self):
        print("{}'s hand:".format(self.name))
        for card in self.hand:
            print("    {}".format(card))
        print()


# a = Player("Oh Jun")
# a.add_card(Card())
# a.add_card(Card("six", "hearts"))
# a.print_hand()