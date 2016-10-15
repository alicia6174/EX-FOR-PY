#!/usr/bin/python
import sys
import random

def Game(Again):
    if (Again == 'n'):
        print "Goodbye!"
        sys.exit()
    elif (Again == 'y'):
        print "Let's play Guess the Number."
    Level = raw_input("Pick a difficulty level (1, 2, or 3): ")
    if ((Level.isdigit() != True) or (int(Level) not in range(1,4))):
        sys.exit()
    Ans = random.randint(1,pow(10,int(Level)))
    #Ans = 2

    Input = raw_input("I have my number. What's your guess? ")
    Count = 1
    State = 0
    while (State == 0):
        if (Input.isdigit() != True):
            Input = raw_input("Please input an integer. Guess again: ")
            Count += 1
        elif (int(Input) < Ans):
            Input = raw_input("Too low.  Guess again: ")
            Count += 1
        elif (int(Input) > Ans):
            Input = raw_input("Too high.  Guess again: ")
            Count += 1
        elif (int(Input) == Ans):
            print "You got it in %d guesses!" % Count
            State = 1

Game('y')
Again = raw_input("Play again? ")
Game(Again)

