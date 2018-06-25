'''
Created on Jun 25, 2018

@author: yo boi konstantin
'''
fibs = []
def fibonacci(num1,num2,egg,timer):
    fibs.append(num2)
    num3 = num2
    num2 = num2 + num1
    num1 = num3
    print(num1,num2,num3)
    egg = egg+1
    if egg > timer:
        return
    fibonacci(num1,num2,egg,timer)

fibonacci(1,1,0,20)
print(fibs)
