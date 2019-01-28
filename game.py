from deck import *
from player import *

class Game:
    def __init__(self, players, buy_in=0, deck = Deck()):
        # players specification:
            # last player is dealer
            # first player is small blind
            # second player is big blind
        self.players = []
        self.deck = deck
        self.pot = 0
        self.community_cards = [] # face up cards

        # Important to shuffle the deck!
        self.deck.shuffle()

        # Add players to self.players
        for player in players:
            self.players.append(player)
        
        # Initialize bank of players to buy_in
        for player in self.players:
            player.set_bank(buy_in)
    
    def print_players(self):
        print("Players:")
        for player in self.players:
            print("    {}".format(player.get_name()))
        print()
    
    def print_players_bank(self):
        print("Players:")
        for player in self.players:
            print("    {}: {}".format(player.get_name(), player.get_bank()))
        print()

    def print_players_hand(self):
        print("Players:")
        for player in self.players:
            print("    {}:".format(player.get_name()))
            for card in player.get_hand():
                print("        {}".format(card))
        print()      

    def print_deck(self):
        self.deck.print_deck()

    def print_community(self):
        print("Community cards:")
        for card in self.community_cards:
            print("    {}".format(card))
        print()

    ###
    ### Game operation
    ###

    def burn(self):
        self.deck.remove_top()

    def add_to_community(self):
        self.community_cards.append(self.deck.get_top())
        self.deck.remove_top()

    # first three community cards
    def flop(self):
        self.burn()
        for i in range(3):
            self.add_to_community()
    
    # fourth community card
    def turn(self):
        self.burn()
        self.add_to_community()

    # fifth community card
    def river(self):
        self.burn()
        self.add_to_community()

    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                player.add_to_hand(self.deck.get_top())
                self.deck.remove_top()
    
    def change_dealer(self):
        first = self.players[0]
        self.players.pop(0)
        self.players.append(first)

a = Game([Player("Alice"), Player("Bob"), Player("Charlie")])

# a.print_deck()
# a.deal_cards()
# a.print_players_hand()
# a.print_deck()

# a.print_players()
# a.change_dealer()
# a.print_players()

# a.print_players_bank()
# a.print_deck()
# a.print_community()
# a.flop()
# a.print_deck()
# a.print_community()