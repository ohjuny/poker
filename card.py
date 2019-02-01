class Card:
    ranks = [
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
        "Ace"
    ]
    suits = [
        "Spades",
        "Clubs",
        "Diamonds",
        "Hearts"
    ]
    def __init__(self, rank="Ace", suit="Spades"):
        self.rank = rank.capitalize()
        self.suit = suit.capitalize()

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    # Override equal to
    def __eq__(self, rhs):
        if (self.suit == rhs.suit and self.rank == rhs.rank):
            return True
        return False

    # Override less than
    def __lt__(self, rhs):
        # Check equal
        if self == rhs:
            return False
        
        # Check less than 
        for rank in Card.ranks:
            if self.rank == rank:
                return True
            if rhs.rank == rank:
                return False

    # Override print
    def __str__(self):
        return self.rank + " of " + self.suit

###


# a = Card()
# b = Card("seven", "spades")
    
# print(a)
# print(b)
# print(a < b)
# print(b < a)