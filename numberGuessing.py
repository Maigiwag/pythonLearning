#numberGuessing.py

'''
Title: Number Guessing game
Author: Jason Wang
Date-Created: 2023-02-07
'''

import random 


#Demonstration code

for i in range(10):
    x = random.randint(1,10)
    print(x)

'''
The function random.randint(x,y) will select a random number from the given range
x-y. You can then assign this randomly generated number from the given range onto a variable. 
The code above selectes a random number from 1-10 and then prints it into the terminal, this is 
reapeated 10 times. 
for i in range is not needed to created a number guessing game. 
'''
