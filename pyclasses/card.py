'''
Created on Jun 25, 2018

@author: yo boi konstantin
'''
class card:
    def __init__(self,number,suit):
        self.suit = suit
        self.number = number
    def getsuit(self):
        return self.suit
    def getnum(self):
        return self.number
    def toString(self):
        return  str(self.number) + ''+ str(self.suit)
    