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
    def __str__(self):
        return  str(self.number) + ''+ str(self.suit)
    def __repr__(self):
        return self.__str__()
    