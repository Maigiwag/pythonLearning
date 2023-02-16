#hangman.py

'''
Title: Hangman Program 
Author: Jason Wang
Date-Created: 2023-02-13
'''

import random

theMan = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]


words = ['HELLO',]



class hangman():

    def __init__(self, wordToGuess):
        self.failedAttempts = 0
        self.wordToGuess = wordToGuess
        self.gameProgress = list('_' * len(self.wordToGuess))
    
    
    




if __name__ == "__main__":
    wordToGuess = random.choice(words)
    hangmanGame = hangman(wordToGuess)