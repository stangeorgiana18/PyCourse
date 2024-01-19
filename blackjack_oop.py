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

    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                # that's the deck: list with card classes
                self.deck.append(Card(suit, rank)) 
            
    def __str__(self):
        deck_components = '' 
        for card in self.deck:
            # add each card object's print string
            deck_components += '\n' + card.__str__()  # the string representation of each card
        
        return 'The deck has: ' + deck_components
        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop() # return a single card
    

test_deck = Deck()
test_deck.shuffle()
print(test_deck)
print('\n')

# representation of a player 
class Hand:

    def __init__(self):
        self.cards = [] # all cards each player has
        self.value = 0 # start with zero value
        self.aces = 0 # add an attribute to keep track of aces

    def add_card(self, card):

        # card passed in
        # from Deck.deal() ---> single Card(suit, rank)

        self.cards.append(card)
        self.value += values[card.rank]

        # track aces 
        if card.rank == 'Ace': # if the player has an ace, the value +=11
            self.aces += 1 

    def adjust_for_ace(self):

        # stay under 21
        # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        # THEN CHANGE MY ACE TO BE A 1 INSTEAD OF 11
        # we're using an integer as thruthiness 
        # treating the .aces integer as a boolean value

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

'''
# check if I can add 2 card to a player's hand and obtain their value
test_deck = Deck()
test_deck.shuffle()

# PLAYER 
test_player = Hand()
# deal 1 card from the deck Card(suit, rank)
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value, '\n')

# see what those cards are 
for card in test_player.cards:
    print(card)

'''

class Chips:

    def __init__(self, total = 100):
        self.total = total # this can be set to a default value or supplied by a user input
        self.bet = 0 # bet value in chips

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# function for taking bets
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips are you betting on?: "))
        except:
            print("Provide an integer.")
        else:
            # if they provided an integer 
            if chips.bet > chips.total:
                print("You don't have enough chips! You have {}".format(chips.total))
            else:
                break


# function for taking hits
# called during gameplay anytime a player requests a hit
# or a Dealer's hand is less than 17
def hit(deck, hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# assign playing as a global variable
def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s: ")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands. Dealer's Turn.")
            playing = False

        else:
            print("I didn't understand that, please enter h or s only!")
            continue
        break


# functions to display cards
# When the game starts, and after each time Player takes a card,
# the dealer's first card is hidden and all of Player's cards are visible
# At the end of the hand all cards are shown, and you may want to show each hand's total value
    
def show_some(player, dealer):

    # dealer.cards[1]

    # show only ONE of the dealer's hand
    print("\n DEALER'S HAND: ")
    print("First card hidden!")
    print(dealer.cards[1])

    # show all (2 cards) of the player's hand/cards
    print("\n PLAYER'S HAND: ")

    for card in player.cards:
        print(card)


def show_all(player, dealer):

    # show all the dealer's cards
    print("\n DEALER'S HAND: ")
    for card in dealer.cards:
        print(card)

    '''
    savvy way with * --> loop through every item and print it out:

    print("\n Dealer's hand: ", *dealer.cards, sep = '\n')
    '''

    # calculate and display value (Jack + King == 20)
    print(f"Value of Dealer's hand is: {dealer.value}")

    # show all the player's cards
    print("\n PLAYER'S HAND: ")
    for card in player.cards:
            print(card)

    print(f"Value of Player's hand is: {player.value}")

# example of * use in looping instead of for 
# functionality inside the print function
items = [1, 2, 3]
print("Items are: ", *items, sep = '\n')


# functions to handle end of game scenarios


def player_busts(player, dealer, chips):
    print("PLAYER BUSTS!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()

# when both players get 21
def push(player, dealer):
    print("Dealer and Player tie! PUSH!")
    

while True:

    # print an opening statements
    print("\n WELCOME TO BLACKJACK! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.")

    # create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up the Player's chips
    player_chips = Chips()

    # prompt the Player for their bet
    take_bet(player_chips)

    # show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing: # recall this variable from the hit_or_stand function

        # prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # if Player's hand > 21 run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break  


    # if Player hasn't busted, play Dealer's hand until it reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

            # show all cards
            # since the dealer is now playing, we need to show all his cards
        show_all(player_hand, dealer_hand)

        # run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            # if both happen to get 21
            push(player_hand, dealer_hand)

        
    # inform Player of their chips total
    print("\n Player total chips are at: {}".format(player_chips.total))

    # ask to play again
    new_game = input("Whould you like to play another hand? y/n: ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing. Hopefully you had fun!")
        break
