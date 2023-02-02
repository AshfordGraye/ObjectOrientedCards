import random

def DiceRoll():
    dice = random.randint (1,6)
    print (dice)
    input ("press enter to roll again")
    DiceRoll()
DiceRoll()