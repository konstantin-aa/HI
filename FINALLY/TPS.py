'''
Created on Jun 27, 2018

@author: yo boi kon
'''
import random

choices = ['rock', 'paper','scissors']
p1 = 0
p2= 0
p1w = 0
p2w = 0
game = 0
while game != 'no':
    game = input('=====Enter To Start, no to stop!=====')
    if game == 'no':
        break
    p1 = int(input('----1 for rock, 2 for paper 3 for scissors!----'))
    p2 = random.randint(1,4)
    if p1 == 1 and p2 == 2:
        print('You chose rock, Computer chose paper ')
        print('%%%% You lost ! %%%%')
        p1w = p1w - 1
        p2w = p2w + 2
    if p1 == 2 and p2 == 1:
        print('You chose paper, Computer chose rock ')
        print('%%%% You won ! %%%%')
        p1w = p1w + 2
        p2w = p2w - 1
    if p1 == 1 and p2 == 3:
        print('You chose rock, Computer chose scissors ')
        print('%%%% You won ! %%%%')
        p1w = p1w + 2
        p2w = p2w - 1
    if p1 == 3 and p2 == 1:
        print('You chose scissors, Computer chose rock ')
        print('%%%% You lost ! %%%%')
        p1w = p1w - 1
        p2w = p2w + 2
    if p1 == 3 and p2 == 2:
        print('You chose scissors, Computer chose paper ')
        print('%%%% You won ! %%%%')
        p1w = p1w + 2
        p2w = p2w - 1
    if p1 == 2 and p2 == 3:
        print('You chose paper, Computer chose scissors ')
        print('%%%% You lost ! %%%%')
        p1w = p1w - 1
        p2w = p2w + 2
    if p1 == 1 and p2 == 1:
        print('You chose rock, Computer chose rock ')
        print('%%%% TIE ! %%%%')
        p1w = p1w + 1
        p2w = p2w + 1
    if p1 == 2 and p2 == 2:
        print('You chose paper, Computer chose paper ')
        print('%%%% TIE ! %%%%')
        p1w = p1w + 1
        p2w = p2w + 1
    if p1 == 3 and p2 == 3:
        print('You chose scissors, Computer chose scissors ')
        print('%%%% TIE ! %%%%')
        p1w = p1w + 1
        p2w = p2w + 1
print('==FINAL SCORE==')
print('YOU: ', p1w)
print('COMPUTER: ', p2w)