import random
from collections import defaultdict
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
         'Ace']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

deck = [c + ' of ' + x for c in cards for x in suits]
hands = defaultdict(list)


def get_card():
    card = random.choice(deck)
    deck.remove(card)
    return card


def deal(players):
    if players > 10:
        print('{} is too many players: There can only be up to 10.'.format(
            players))
        return
    for x in range(1, (players + 1)):
        for i in range(1, 6):
            hands[x].append(get_card())
    print(hands)
num_players = input('Please enter a number of players ')
deal(num_players)
