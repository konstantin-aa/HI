'''
Created on Jun 25, 2018

@author: Yo boi konstantin
'''
from deck import deck
feed = 0
Bicicle = deck()
Bicicle.shufffle()
purple = Bicicle.getdeck()
def show():
    print('Your Hand: ')
    for b in range(len(p1)):
        print(p1[b].toString())
    print('Sum: ', p1tot)
    print('Dealer\'s Hand:', p2[0].toString(), ' ',p2[1].toString(), ' Sum: ',p2tot)
while feed != 'quit':
    game = False
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
    p2tot = 0
    while game != True:
        p1tot = 0
        p2tot = 0
        for j in range(len(p1)):
            p1tot = p1tot+p1[j].getnum()
        for l in range(len(p2)):
            p2tot = p2tot+p2[l].getnum()
        print('Your Hand: ')
        for b in range(len(p1)):
            print(p1[b].toString())
        print('Sum: ', p1tot)
        print('Dealer\'s Hand:', p2[0].toString(), '  ? of ?', ' Sum: Who Knows?')
        hs = input('Do you Want to hit or stay? ')
        if hs == 'stay':
            if 21-p1tot > 21-p2tot:
                game = True
                print('DEALER WINS!')
                show()
            if 21-p1tot <21-p2tot:
                print('Player One WINS!')
                show()
                game = True
            if 21-p1tot == 21-p2tot:
                print('TIE!')
                show()
                game = True
                
        if hs == 'hit':
            p1.append(purple[0])
            del purple[0]
        p1tot = 0
        for j in range(len(p1)):
            p1tot = p1tot+p1[j].getnum()
        if len(purple) == 0:
            Bicicle = deck()
            Bicicle.shufffle()
            purple = Bicicle.getdeck()
            game = True
        if p1tot == 21:
            print('Player One WINS!')
            show()
            game = True
        if p1tot > 21:
            game = True
            print('DEALER WINS!')
            show()
            

