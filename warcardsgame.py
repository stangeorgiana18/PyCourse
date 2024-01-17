# create a card class
# understand the suit, rank, value of the card

# Card() - parantheses not necessary since we're not using inheritance
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
two_hearts = Card("Hearts", "Two")

print(two_hearts)

print(two_hearts.rank, two_hearts.suit)

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


print(values[two_hearts.rank])


# deck class 


# player 