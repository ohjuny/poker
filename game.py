from deck import *
from player import *

# To get 7C5 combinations of 7 cards
from itertools import combinations 

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

    ###
    ### Functions that check for specific winning hand
    ###

    # Score
    # (Royal Flush)  : not included because this is just the highest Straight Flush
    # Straight Flush : 8
    # Four of a Kind : 7
    # Full House     : 6
    # Flush          : 5
    # Straight       : 4
    # Three of a Kind: 3
    # Two Pair       : 2
    # One Pair       : 1
    # High Card      : 0

    win_hands = [
        "Straight Flush" : 8,
        "Four of a Kind" : 7,
        "Full House"     : 6,
        "Flush"          : 5,
        "Straight"       : 4,
        "Three of a Kind": 3,
        "Two Pair"       : 2,
        "One Pair"       : 1
        # "High Card"      : 0 # Not needed
    ]

    # # Check if cards in list have same rank
    # def check_same_rank(self, cards):
    #     ranks = set()
    #     for card in cards:
    #         ranks.add(get_rank(card))
    #     return len(ranks) == 1

    # Returns number of cards with given rank
    def count_same_rank(self, cards, rank):
        # Extract ranks of cards
        ranks = extract_ranks(cards)
        rank = Cards.ranks.index(rank) + 2
        return ranks.count(rank)

        # counter = 0
        # for card in cards:
        #     if get_rank(card) == rank:
        #         counter += 1
        # return counter
    
    # Returns highest number of same ranks in cards
    def count_highest_same_rank(self, cards):
        highest = 0
        for card in cards:
            rank_count = count_same_rank(cards, get_rank(card))
            if rank_count > highest:
                highest = rank_count
        return highest

    # Returns list of integers representing ranks
    def extract_ranks(self, cards):
        # Extract ranks of cards
        ranks = [get_rank(card) for card in cards]
        # Convert to integer by using index in Cards.rank
        return [Cards.ranks.index(rank) + 2 for rank in ranks]
        # Note: J = 11, Q = 12, K = 13, A = 14

    # All functions receive 5 cards
    # All functions return Boolean (True, False)

    def check_straight_flush(self, cards):
        return check_straight(cards) and check_flush(cards)

    def check_four_kind(self, cards):
        return count_highest_same_rank(cards) == 4

    def check_full_house(self, cards):
        # Extract ranks of cards
        ranks = extract_ranks(cards)
        # Full House would reduce to length 2
        if len(set(ranks)) != 2:
            return False
        # Ensures it's not a Four of a Kind
        return count_highest_same_rank(cards) == 3

    def check_flush(self, cards):
        suits = set()
        for card in cards:
            suits.add(get_suit(card))
        return len(suits) == 1

    def check_straight(self, cards):
        # Extract ranks of cards
        ranks = extract_ranks(cards)
        ranks.sort()
        # Ranks must be unique in a straight
        if len(set(ranks)) != 5:
            return False
        # Smallest number in straight must be 10 or lower
        if ranks[0] > 10:
            return False

        # Account for when A is used as 1
        if ranks[0] == 2 and ranks[4] == 14:
            return ranks[3] == 5
        
        # General case
        return ranks[4] - ranks[0] == 4

    def check_three_kind(self, cards):
        return count_highest_same_rank(cards) == 3

    def check_two_pair(self, cards):
        # Extract ranks of cards
        ranks = extract_ranks(cards)
        # Two pairs would reduce to length 3
        if len(set(ranks)) != 3:
            return False
        # Ensures it's not a Three of a Kind
        return count_highest_same_rank(cards) == 2

    def check_pair(self, cards):
        # Extract ranks of cards
        ranks = extract_ranks(cards)
        return len(set(ranks)) == 4

    # Do I even need to check for high hand? It'll always be true
        
    ###
    ### End of winning hand functions
    ###

    # # Returns score of given 5 cards
    def calulate_score(self, cards):
        if check_straight_flush(cards):
            return 8
        if check_four_kind(cards):
            return 7
        if check_full_house(cards):
            return 6
        if check_flush(cards):
            return 5
        if check_straight(cards):
            return 4
        if check_three_kind(cards):
            return 3
        if check_two_pair(cards):
            return 2
        if check_pair(cards):
            return 1
        # High card
        return 0

    # Returns list of best 5 cards given 7 cards given score
    def calculate_best_hand(self, cards, score):
        # TO DO
        return

    # Returns best score for given player
    def calculate_player_score(self, player):
        # Combine player hand with community cards
        cards = get_hand(player) + self.community_cards

        # Calculate every combination (5) of 7 cards
        possible_hands = combinations(cards, 5)
        possible_hands = [list(hand) for hand in possible_hands]

        # Find highest score of possible_hands
        highest = 0
        for hand in possible_hands:
            score = calulate_score(hand)
            if score > highest:
                highest = score
        
        return highest
    
    # Updates player.score for all players
    def calculate_all_scores(self):
        for player in players:
            # Updates player.score to reflect best hand
            set_score(player, self.calculate_player_score(player))

    # Checks how good a hand is
    def find_winner(self):
        # Updates player.score for all players
        self.calculate_all_scores()

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