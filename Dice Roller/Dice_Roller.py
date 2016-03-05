#Build 1.0.0

from sys import exit
from random import randint

def getDiceNumber():
    try:
        diceNumber = int(input('Enter Number of Die to Roll: '))
        return diceNumber
    except ValueError:
        print('Error: Enter a numerical value.')
        getDiceNumber()

def getDiceSides():
    try:
        diceSides = int(input('Enter Number of Sides per Die: '))
        return diceSides
    except ValueError:
        print('Error: Enter a numerical value.')
        getDiceSides()

def rollDice(diceNumber, diceSides):
    total = 0
    while diceNumber > 0:
        roll = randint(1, diceSides)
        total += roll
        print('Die {}: {}'.format(diceNumber, roll))
        diceNumber -= 1
    return total

def main():
    diceNumber = getDiceNumber()
    diceSides = getDiceSides()
    print('Total Value: {}'.format(rollDice(diceNumber, diceSides)))
    input('Press Enter to close...')

if __name__ == "__main__":
    exit(int(main() or 0))