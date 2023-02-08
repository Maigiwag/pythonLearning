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

another bit of code you might need will be the if statement:

if "input" > x:
    print("your number is greater than the target number")

if "input" < x: 
    print("Your number is lower than the target number")


OBJECTIVE:
The goal is to create a number guessing game where the program will randomly generate a number
from a range of your choosing. The user will then be prompted to guess a random number, 
the program will inform the user if their guess is higher or lower than the target number
generated by the program. The program will loop until user guesses number, and then will be asked
if they want to play again or exit the program. Adding a points counter is possible if you would like.

'''








