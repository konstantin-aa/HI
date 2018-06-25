'''
Created on Jun 25, 2018

@author: yo boi konstantin
'''

def facs(fac,ramp,increment,key):
    key = key * ramp
    ramp = ramp + increment
    if ramp > fac:
        print(key)
        return
    facs(fac,ramp,increment,key)

facs(8,2,2,1)