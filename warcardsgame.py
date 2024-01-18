# create a CARD CLASS
# understand the suit, rank, value of the card

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# Card() - parantheses not necessary since we're not using inheritance
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
two_hearts = Card("Hearts", "Two")


# print(two_hearts)
# print(two_hearts.rank, two_hearts.suit)
# print(values[two_hearts.rank])
# three_of_clubs = Card("Clubs", "Three")
# print(three_of_clubs.value)
# print(three_of_clubs.value > three_of_clubs.value)


# DECK CLASS 

# instantiate the class

class Deck():

    def __init__(self):
        # user input unrequired, every new deck should be the same
        # as the previous instance of a deck previously instantiated
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # create the card object
                created_card = Card(suit, rank) # create a new deck

                self.all_cards.append(created_card)

    def shuffle(self):
        # internally shuffle all the cards; shuffle doesn't return anything
        random.shuffle(self.all_cards) 

    def deal_one(self):
        # grab one card from somewhere in the list
        return self.all_cards.pop()


'''
new_deck = Deck()
first_card = new_deck.all_cards[0]
print(first_card) # Two of Hearts
bottom_card = new_deck.all_cards[-1]
print(bottom_card) # Ace of Clubs

# print all the cards 
# all_cards hold various card objects, which recalled, return their rank and suit

for card_object in new_deck.all_cards:
    print(card_object)
'''

new_deck = Deck()
new_deck.shuffle()
print(new_deck.all_cards[-1]) # Six of Clubs for eg.


new_deck.shuffle()
mycard = new_deck.deal_one()
print(mycard) # Five of Diamonds
print(len(new_deck.all_cards)) # 51 now




# player 

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = [] # empty hand for each player 

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # for a single card object
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


new_player = Player("Geo")
print(new_player)

new_player.add_cards(mycard)

print(new_player) # Player Geo has 1 cards.
print(new_player.all_cards[0]) # Two of Clubs

new_player.add_cards([mycard, mycard, mycard])
print(new_player) # Player Geo has 4 cards.
new_player.remove_one()
print(new_player) # Player Geo has 3 cards.

