import random

class Dice():

    def __init__(self, numsides):
          self.numsides = numsides
    def DiceRoll(self):
        roll = random.randint (1,self.numsides)
        print (roll)

# sixside = Dice(6)
# twelveside = Dice(12)

# def run():
#     sixside.DiceRoll()
#     twelveside.DiceRoll()
#     input("press enter to roll again")
#     run()
# run()