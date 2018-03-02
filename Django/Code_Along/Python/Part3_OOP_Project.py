#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

import random

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.cards = [];
        for s in SUITE:
            for r in RANKS:
                self.cards.append(s+r)


    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def split(self):
        return[self.cards[:26],self.cards[26:]]


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, cards):
        self.cards = cards
    def __str__(self):
        return str(self.cards)

    def addCards(self, cards):
        self.cards.append(cards)

    def removeCards(self, card):
        self.cards.remove(card)

    def pick_card(self):
        return self.cards.pop(0)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, hand):
        self.hand = hand

    def __str__(self):
        return str(self.hand)

    def pick_card(self):
        return self.hand.pick_card()

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
the_deck = Deck()
the_deck.shuffle()
card_stacks = the_deck.split()

hand1 = Hand(card_stacks[0])
hand2 = Hand(card_stacks[1])

player1 = Player(hand1)
player2 = Player(hand2)

card1 = player1.pick_card()
card2 = player2.pick_card()

if compare_cards(card1,card2) ==1
    player1.addCards(card1+card2)
elif compare_cards(card1,card2) == -1
    player2.addCards(card1+card2)
elif compare_cards(card1,card2) == 0
    cards1 = []
    cards2 = []
    for i in range(3):
        cards1.append(player1.pick_card())
        cards2.appedn(player2.pick_card())


def compare_cards(card1, card2):
    if RANKS.index(card1[1]) > RANKS.index(card2[1]):
        return 1
    elif RANKS.index(card1[1]) < RANKS.index(card2[1]):
        return -1
    elif RANKS.index(card1[1]) == RANKS.index(card2[1])
        return 0
# Use the 3 classes along with some logic to play a game of war!
