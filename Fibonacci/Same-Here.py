'''
Created on Jun 25, 2018

@author: Yo Boi Konstantin


'''
numlist = [1,1]

for x in range(1,100):
    numlist.append(numlist[x]+numlist[x-1])
print(numlist)

