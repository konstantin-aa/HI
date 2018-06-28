'''
Created on Jun 25, 2018

@author: yo boi konstantin
'''
from card import card
import random
class deck:
    def __init__(self):
        self.deck = []
        for x in range(2,15):
            self.deck.append(card( x, ' of spades'))
        for y in range(2,15):
            self.deck.append(card(y, ' of clubs' ))
        for z in range(2,15):
            self.deck.append(card(z, ' of diamonds' ))
        for xx in range(2,15):
            self.deck.append(card( xx,' of hearts')) 
    def toString(self):
        for x in self.deck:
            print(x.toString())
    def shufffle(self):
        deck2 = self.deck
        self.deck = []
        for x in range(len(deck2)):
            ha = random.randint(0,len(deck2)-1)
            self.deck.append(deck2[ha])
            del deck2[ha]
    def getdeck(self):
        return self.deck
