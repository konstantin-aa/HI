'''
Created on Jun 26, 2018

@author: yo boi kohstantin
'''

from deck2 import deck
gtry = 'yes'

while gtry == 'yes':
    feed = 0
    p1d = []
    p2d = []
    Bicicle = deck()
    Bicicle.shufffle()
    purple = Bicicle.getdeck()
    p1 = []
    for x in range((int(len(purple)/2))):
        p1.append(purple[0])
        del purple[0]
    p2 = purple
    game = True
    while game == True:
        check = input('===Press enter to start up cards, q to quit===')
        def stack(player):
            print('HIII')
            if player == 1:
                for asd in range(len(p1d)):
                    p1.append(p1d[0])
                    del p1d[0] 
            if player == 2:
                for abc in range(len(p2d)):
                    p2.append(p2d[0])
                    del p2d[0]
        def chek(player,thresh):
            if player == 1:
                if len(p1) - thresh <= 0:
                    stack(1)
            if player == 2:
                if len(p2) - thresh <= 0:
                    stack(2)
        if check == 'q':
            game = False
            gtry = 'no'
        chek(1,1)
        chek(2,1)
        drew1 = p1[0]
        drew2 = p2[0]  
        print('Player 1 Drew: ', drew1.toString())
        print('Player 2 Drew: ', drew2.toString())
        if drew1.getnum() > drew2.getnum():
            print('PLAYER 1 PICKS UP CARDS! ')
            p1d.append(drew1)
            p1d.append(drew2)
            del p1[0]
            del p2[0]
        elif drew1.getnum() < drew2.getnum():
            print('PLAYER 2 PICKS UP CARDS! ')
            p2d.append(drew1)
            p2d.append(drew2)
            del p1[0]
            del p2[0]
        else:
            warq = 0
            stwar = 1
            while warq == 0:
                stwar = stwar + 5
                chek(1,stwar)
                chek(2,stwar)
                print('=====WAR!=====')
                drew1 = p1[stwar]
                drew2 = p2[stwar]
                print('Player 1 Drew: ', drew1.toString())
                print('Player 2 Drew: ', drew2.toString())
                if drew1.getnum() > drew2.getnum():
                    print('Player 1 picks up cards! ')
                    for jk in range(stwar+1):
                        p1d.append(p1[jk])
                        p1d.append(p2[jk])
                        del p2[jk]
                        del p1[jk]
                    warq = 1
                elif drew1.getnum() < drew2.getnum():
                    print('Player 2 picks up cards! ')
                    for jh in range(stwar+1):
                        p2d.append(p1[jh])
                        p2d.append(p2[jh])
                        del p2[jh]
                        del p1[jh]
                    warq = 1
        print('=====INFO!=====')
        print('=====Player 1=====')
        print('Pile: ', len(p1))
        print('Discard: ', len(p1d))
        print('TOTAL: ', len(p1) + len(p1d))
        print('=====Player 2=====')
        print('Pile: ', len(p2))
        print('Discard: ', len(p2d))
        print('TOTAL: ', len(p2) + len(p2d))
            

print('Bye!!')
        
    
