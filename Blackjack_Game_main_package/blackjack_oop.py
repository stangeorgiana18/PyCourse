# one player versus an automated dealer

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        # self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                # create the card object
                created_card = Card(suit, rank)
                # that's the deck
                self.deck.append(created_card) 
            
    def __str__(self):
        deck_components = '' 
        for card in self.deck:
            # add each card object's print string
            deck_components += '\n' + card.__str__() 
        
        return 'The deck has: ' + deck_components
        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
    

# test_deck = Deck()
# print(test_deck)


class Hand:

    def __init__(self):
        self.cards = [] # all cards each player has
        self.value = 0 # start with zero value
        self.aces = 0 # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        pass

test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print(test_player.value)