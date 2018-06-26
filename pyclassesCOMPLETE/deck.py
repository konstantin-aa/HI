'''
Created on Jun 25, 2018

@author: yo boi konstantin
'''
from card import card
import random
class deck:
    def __init__(self):
        self.deck = []
        for x in range(1,11):
            self.deck.append(card( x, ' of spades'))
        for x2 in range(1,4):
            self.deck.append(card( 10, ' of spades'))
        for y in range(1,11):
            self.deck.append(card(y, ' of clubs' ))
        for y2 in range(1,4):
            self.deck.append(card( 10, ' of clubs'))
        for z in range(1,11):
            self.deck.append(card(z, ' of diamonds' ))
        for z2 in range(1,4):
            self.deck.append(card( 10, ' of diamonds'))
        for xx in range(1,11):
            self.deck.append(card( xx,' of hearts')) 
        for xx2 in range(1,4):
            self.deck.append(card( 10, ' of hearts'))
    def toString(self):
        for x in self.deck:
            print(x.toString())
    def shufffle(self):
        deck2 = self.deck
        self.deck = []
        for x in range(len(deck2)-1):
            self.deck.append(deck2[random.randint(0,len(deck2)-1)])
    def getdeck(self):
        return self.deck
