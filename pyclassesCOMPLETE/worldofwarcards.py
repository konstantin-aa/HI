'''
Created on Jun 26, 2018

@author: yo boi kohstantin
'''

from deck2 import deck
gtry = 'yes'
w1 = 0
w2 = 0
check = 0
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
    p2 = purple
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
        if player == 1:
            if len(p1)+len(p1d) < thresh:
                print(thresh)
                game = 'xd'
                print('PLAYER 2 WINS!!!')
                w2 = w2+1
                return
            if len(p1) < thresh:
                stack(1)
        if player == 2:
            if len(p2)+len(p2d) < thresh:
                game = 'xd'
                print(thresh)
                print('PLAYER 1 WINS!!!') 
                w1 = w1+1
                return
            if len(p2) < thresh:
                stack(2)
    while game == 'lol':
        check = check+1
        print(check)
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
            #print('Player 1 Drew: ', drew1.toString())
            #print('Player 2 Drew: ', drew2.toString())
            if drew1.getnum() > drew2.getnum():
                #print('PLAYER 1 PICKS UP CARDS! ')
                p1d.append(drew1)
                p1d.append(drew2)
            elif drew1.getnum() < drew2.getnum():
                #print('PLAYER 2 PICKS UP CARDS! ')
                p2d.append(drew1)
                p2d.append(drew2)
            else:
                warq = 0
                stwar = 0
                pp1 = 0
                pp2 = 0
                stw1 = 0
                stw2 = 0
                drew1 = []
                drew2 = []
                while warq == 1000:
                    print('this is warq: ',warq)
                    stwar = stwar + 4
                    stw1 = stwar
                    stw2 = stwar
                    if len(p1)+len(p1d) < stwar+1 and len(p1)+len(p1d) > 0:
                        stw1 =  (len(p1)+len(p1d)-2)
                        print('work')
                        stack(1)
                    else:
                        chek(1,stw1+1,w1,w2)
                        chek(2,stw1+1,w1,w2)
                    if len(p2)+len(p2d) < stwar+1 and len(p2)+len(p2d) > 0:
                        stw2 = (len(p2)+len(p2d)-2)
                        print('work')
                        stack(2)
                    else:
                        chek(1,stw1+1,w1,w2)
                        chek(2,stw2+1,w1,w2)
                    if game == 'lol':
                        #print('=====WAR!=====')
                        for x in range(stw1+1):
                            drew1.append(p1[0])
                            del p1[0]
                        for x in range(stw2+1):
                            drew2.append(p2[0])
                            del p2[0]
                        print(drew1)
                        print(drew2)
                        #print('Player 1 Drew: ', drew1.toString())
                        #print('Player 2 Drew: ', drew2.toString())
                        if drew1[0].getnum() > drew2[0].getnum():
                            #print('Player 1 picks up cards! ')
                            for jk in range(stw1-2):
                                if game == 'lol':
                                    p1d.append(drew1[0])
                                    p1d.append(drew2[0])
                                    del drew1[0]
                                    del drew2[0]
                            warq = 1
                            print('boi')
                        if drew1[0].getnum() < drew2[0].getnum():
                            #print('Player 2 picks up cards! ')
                            for jh in range(stw2-2):
                                if game == 'lol':
                                    p2d.append(drew1[0])
                                    p2d.append(drew2[0])
                                    del drew1[0]
                                    del drew2[0]
                            warq = 1
                            print('boi')
        #print('=====INFO!=====')
        #print('=====Player 1=====')
        #print('Pile: ', len(p1))
        #print('Discard: ', len(p1d))
        #print('TOTAL: ', len(p1) + len(p1d))
        #print('=====Player 2=====')
        #print('Pile: ', len(p2))
        #print('Discard: ', len(p2d))
        #print('TOTAL: ', len(p2) + len(p2d))
for x in range(1):
    cards()
            

print('Bye!!')
print('Player 1 won:', w1, ' times')
print('Player 2 won:', w2, ' times')
    
