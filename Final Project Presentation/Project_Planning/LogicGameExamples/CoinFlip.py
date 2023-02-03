import random

def CoinFlip():
    flip = random.randint (1,2)
    if flip == 1:
        print ("Heads")
    if flip == 2:
        print ("Tails")
    input ("press enter to flip again")
    CoinFlip()
CoinFlip()