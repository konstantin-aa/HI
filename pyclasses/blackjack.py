'''
Created on Jun 25, 2018

@author: Yo boi konstantin
'''
from deck import deck
feed = 0
Bicicle = deck()
Bicicle.shufffle()
purple = Bicicle.getdeck()

while feed != 'quit':
    feed = input('Do you want to quit? Type Q to quit or skip this to continue: ')
    p1 = [purple[0]]
    del purple[0]
    p2 = [purple[0]]
    del purple [0]
    p1.append(purple[0])
    del purple[0]
    p2.append(purple[0])
    del purple[0]
    p1tot = 0
    for j in range(len(p1)):
        p1tot = p1tot+p1[j].getnum()
    print('Your Hand: ',p1[0].toString(),' ',p1[1].toString(), ' Sum: ', p1tot)
    print('Dealer\'s Hand:', p2[0].toString(), '  ?', ' Sum: Who Knows?')
    hs = input('Do you Want to hit or stay? ')
    if hs == 'stay':
        pass
    if hs == 'hit':
        p1.append(purple[0])
        del purple[0]
        