'''
Created on Jun 26, 2018

@author: yo boi kohstantin
'''

from deck2 import deck
from numpy.random.mtrand import shuffle
gtry = 'yes'
w1 = 0
w2 = 0
check = 0
f1 = 0
f2 = 0
def cards():
    global game
    global check
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
    print(p1)
    p2 = purple
    print(p2)
    print(len(p1))
    print(len(p2))
    game = 'lol'
    print('hi')
    def stack(player):
            global game
            if player == 1:
                for asd in range(len(p1d)):
                    p1.append(p1d[0])
                    del p1d[0] 
            if player == 2:
                for abc in range(len(p2d)):
                    p2.append(p2d[0])
                    del p2d[0]
    def chek(player,thresh,w1,w2):
        global game
        global f1
        global f2
        if player == 1:
            if len(p1)+len(p1d) < thresh:
                print("thresh: ", thresh)
                game = 'xd'
                print('PLAYER 2 WINS!!!')
                f2 = f2+1
                return
            if len(p1) < thresh:
                stack(1)
        if player == 2:
            if len(p2)+len(p2d) <thresh:
                game = 'xd'
                print("thresh", thresh)
                print('PLAYER 1 WINS!!!') 
                f1 = f1+1
                return
            if len(p2) < thresh:
                stack(2)
    while game == 'lol':
        if game != 'lol':
            warq = 1
        if check == 'q':
            game = 'xd'
            gtry = 'no'
        chek(1,1,w1,w2)
        chek(2,1,w1,w2)
        if game == 'lol':
            drew1 = p1[0]
            drew2 = p2[0]  
            del p1[0]
            del p2[0]
            if game != 'lol':
                warq = 1
            print(game)
            shuffle(p1)
            shuffle(p2)
            chek(1,1,w1,w2)
            chek(2,1,w1,w2)
            #print('Player 1 Drew: ', drew1)
            #print('Player 2 Drew: ', drew2)
            if drew1.getnum() > drew2.getnum():
                #print('PLAYER 1 PICKS UP CARDS! ')
                p1d.append(drew1)
                p1d.append(drew2)
                print(drew1,drew2)
                print('no')
            elif drew1.getnum() < drew2.getnum():
                #print('PLAYER 2 PICKS UP CARDS! ')
                p2d.append(drew1)
                p2d.append(drew2)
                print('yes')
            else:
                warq = 0
                stwar = 0
                pp1 = 0
                pp2 = 0
                stw1 = 0
                stw2 = 0
                drew1 = []
                drew2 = []
                while warq == 0:
                    print('this is warq: ',warq)
                    stwar = stwar + 4
                    stw1 = stwar
                    stw2 = stwar
                    print(stwar)
                    if game != 'lol':
                        warq = 1
                    if game == 'lol':
                        chek(1,stwar+1,w1,w2)
                        chek(2,stwar+1,w1,w2)
                        if game != 'lol':
                            warq = 1
                        if game == 'lol':
                            #print('=====WAR!=====')
                            for x in range(stwar):
                                drew1.append(p1[0])
                                del p1[0]
                            for n in range(stwar):
                                drew2.append(p2[0])
                                del p2[0]
                            print(drew1)
                            print(drew2)
                            
                            #print('Player 1 Drew: ', drew1.toString())
                            #print('Player 2 Drew: ', drew2.toString())
                            if len(drew1) != 0 and len(drew2) != 0:
                                if drew1[-1].getnum() > drew2[-1].getnum():
                                    #print('Player 1 picks up cards! ')
                                    for jp in range(len(drew1)):
                                        if game == 'lol':
                                            p2d.append(drew1[0])
                                            del drew1[0]
                                    for jh in range(len(drew2)):
                                        p2d.append(drew2[0])
                                        del drew2[0]
                                    warq = 1
                                    print('boi')
                            if len(drew1) != 0 and len(drew2) != 0:
                                if drew1[-1].getnum() < drew2[-1].getnum():
                                    #print('Player 2 picks up cards! ')
                                    for jz in range(len(drew1)):
                                        if game == 'lol':
                                            p2d.append(drew1[0])
                                            del drew1[0]
                                    for ja in range(len(drew2)):
                                        p2d.append(drew2[0])
                                        del drew2[0]
                                    warq = 1
                                    print('boi')
                            chek(1,stw2+2,w1,w2)
                            chek(2,stw2+2,w1,w2)
        #print('=====INFO!=====')
        #print('=====Player 1=====')
        #print('Pile: ', len(p1))
        #print('Discard: ', len(p1d))
        #print('TOTAL: ', len(p1) + len(p1d))
        #print('=====Player 2=====')
        #print('Pile: ', len(p2))
        #print('Discard: ', len(p2d))
        #print('TOTAL: ', len(p2) + len(p2d))
for x in range(1000):
    cards()
            

print('Bye!!')
print('Player 1 won:', f1, ' times')
print('Player 2 won:', f2, ' times')
    
