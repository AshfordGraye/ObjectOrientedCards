import random

class Card:

    #initalised with the card
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number
        if self._number in [str(n) for n in range (2,11)]:
            self._value = int(number)
        elif self._number in ["Jack","Queen","King"]:
            self._value = 10
        elif self.number in ["Ace"]:
            self._value = 1


    #how the card is represented on screen
    def __repr__(self):
        return (f"{self._number} of {self.suit}")
    
    #defines the card's suit as a property of the card class
    @property
    def suit (self):
        return self._suit

    #defines the card's number as a property
    @property
    def number (self):
        return self._number

    # a setter initalises a variable against a condition - this one check to see if an assigned suit is real 
    @suit.setter
    def suit (self, suit):
        if suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            self._suit = suit
        else:
            print ("That's not a real card suit!")
    
    # this setter checks to see if the assigned card is real
    @number.setter
    def number (self, number):
        if number in  [str(n) for n in range (2,11)]:
            self._number = number
        elif number in ["Jack","Queen","King","Ace"]:
            self._number = number
        else:
            print ("That isn't a real card!")
    
# the deck class popoulates a list with instances of cards
class Deck:
    #upon initialisation, creates a self-referring list of cards, populates the list and prints the list
    def __init__(self):
        self._cards = []
        self.populate()
    #function called during init to create instance of the cards
    def populate (self):
        #define the suits and cards to populate the deck with (Is this how fictional card games like Pazaak were created?)
        suits = ["Hearts","Diamonds","Clubs","Spades"]
        numbers = [str(n) for n in range (2,11)] + ["Jack","Queen","King","Ace"]

        #in the cards list
        cards = []
        #for every suit in the list defined earlier
        for suit in suits:
            #and then for every number
            for number in numbers:
                #add the cards suit and number 
                cards.append (Card(suit,number))
        #and so the cards list will equal the cards!
        self._cards = cards



# initialise a deck of Cards
mydeck = Deck()

# Printing the Deck
def ShowTheDeck():
    print (f"The deck has: {str(mydeck._cards)} \n")

# Shuffling the Deck
def ShuffleTheDeck():
    for i in range(len(mydeck._cards)-1, 0, -1):
        
        # Pick a random index from 0 to i
        j = random.randint(0, i + 1)
    
        # Swap arr[i] with the element at random index
        mydeck._cards[i], mydeck._cards[j] = mydeck._cards[j], mydeck._cards[i]



# sstep 1
# initialise a Hand object
class Hand:
    def __init__(self, handvalue): #tell it to have self referential hand value
        self.cards = []
        self.handvalue = handvalue

#step 2
#create a hand for the cards to go into - remember the hand is  worth 0 when starting a game!
myhand = Hand(0)
otherhand = Hand(0)

#step 3
def MyDeal(): #create a method to deal the card
    takencard = mydeck._cards.pop (0) #pop the card from the list so we can hold it in memory to pull the value
    myhand.handvalue += takencard._value # increase the value of the hand by the value of the card
    myhand.cards.append(takencard)

def OtherDeal():
    takencard = mydeck._cards.pop (0) #pop the card from the list so we can hold it in memory to pull the value
    otherhand.handvalue += takencard._value # increase the value of the hand by the value of the card
    otherhand.cards.append(takencard)

def ShowMyHand():
    print (f"I have {myhand.cards} in my hand")
    print (f"my hand is now worth {myhand.handvalue}\n") #show hand value 

def ShowOtherHand():
    print (f"The cards in the  other hand are {otherhand.cards}")
    print (f"The value of the other hand is {otherhand.handvalue} \n")

# # Let's test it!
# ShuffleTheDeck() #always shuffle the deck before dealing!
# for i in (1,2):
#     MyDeal()
# ShowMyHand()
# for i in (1,2):
#     OtherDeal()
# ShowOtherHand()

###############################################
##### FINAL STAGING AREA FOR PRESENTATION #####
###############################################
#####################################################################################
##### FOLLOWING CODE IS FOR PRESENTATION ONLY AND NOT PART OF THE FINAL PROGRAM #####
##################################################################################### 



import os
import sys
import time

##### THIS CLASS IS STOLEN CODE FROM REPLIT! SHHHHH!
class type():
    def write(text, speed=0.02):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()

            time.sleep(speed)

    print("")

    def clear():
        os.system('clear')
        
    def fg(r,g,b):
        return f'\033[38;2;{r};{g};{b}m'

    def bg(r,g,b):
        return f"\033[48;2;{r};{g};{b}m"

    fg_red = fg(242,78,78)
    fg_orange = fg(255,168,5)
    fg_yellow = fg(249,255,89)
    fg_lightgreen = '\033[92m'
    fg_green = fg(54,200,99)
    fg_lightblue = '\033[94m'
    fg_lightestblue = fg(128,128,255)
    fg_blue = '\033[34m'
    fg_purple = fg(151,71,255)
    fg_brown = fg(190,140,100)
    fg_black = fg(0,0,0)
    fg_silver = fg(191,191,191)

    bg_red = bg(255,0,69)
    bg_orange = bg(255,100,0)
    bg_yellow = bg(255,255,0)
    bg_lightgreen = '\033[102m'
    bg_green = bg(54,150,50)
    bg_lightblue = '\033[104m'
    bg_blue = '\033[44m'
    bg_purple = bg(151,50,250)
    bg_brown = bg(190,100,77)
    bg_silver = bg(163,163,163)

    bold = '\033[1m'
    dim = '\033[2m'
    italic = '\033[3m'
    underline = '\033[4m'
    reverse = '\033[7m'
    invisible = '\033[8m'
    crossover = '\033[9m'
    reset = '\033[0m'

class quicktype():
    def write(text, speed=0.01):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()

            time.sleep(speed)

    print("")

    def clear():
        os.system('clear')
    def fg(r,g,b):
        return f'\033[38;2;{r};{g};{b}m'

    def bg(r,g,b):
        return f"\033[48;2;{r};{g};{b}m"

    fg_red = fg(242,78,78)
    fg_orange = fg(255,168,5)
    fg_yellow = fg(249,255,89)
    fg_lightgreen = '\033[92m'
    fg_green = fg(54,200,99)
    fg_lightblue = '\033[94m'
    fg_lightestblue = fg(128,128,255)
    fg_blue = '\033[34m'
    fg_purple = fg(151,71,255)
    fg_brown = fg(190,140,100)
    fg_black = fg(0,0,0)
    fg_silver = fg(191,191,191)

    bg_red = bg(255,0,69)
    bg_orange = bg(255,100,0)
    bg_yellow = bg(255,255,0)
    bg_lightgreen = '\033[102m'
    bg_green = bg(54,150,50)
    bg_lightblue = '\033[104m'
    bg_blue = '\033[44m'
    bg_purple = bg(151,50,250)
    bg_brown = bg(190,100,77)
    bg_silver = bg(163,163,163)

    bold = '\033[1m'
    dim = '\033[2m'
    italic = '\033[3m'
    underline = '\033[4m'
    reverse = '\033[7m'
    invisible = '\033[8m'
    crossover = '\033[9m'
    reset = '\033[0m'

#####
#####

# These are message classes that format text automatically
class SectionTitle(type):
    def write (mytext):
        quicktype.write(f'{type.fg_blue}{type.bold}{mytext}{type.reset}\n')

class Speaking(type):
    def write (mytext):
        type.write(f'{type.fg_orange}{type.italic}{mytext}{type.reset}\n')


SectionTitle.write ("\nPART 1 - GIVING THE CARDS VALUE   \n")
Speaking.write ("The first step of the guide instructs users on how to add integer values to cards in a deck so they may be used in a card game.    \nTo demonstrate, we will now create two card objects and assign them values to be printed below:  \n")
mycard = Card("Spades", "Ace")
print (mycard)
print (mycard._value)
print()
mycard2 = Card("Hearts", "Queen")
print (mycard2)
print (mycard2._value)
Speaking.write ("\nAs we can see, the cards now have numerical values assigned to them.   \n\n")
SectionTitle.write ("PART 2 - SHUFFLING THE DECK \n")
Speaking.write ("Every card game needs the deck to be shuffled first. Since the cards have been populated into the deck in order, Step 2 instructs users on how they can shuffle the card objects in the deck. \nFirst, we will show the populated deck, then shuffle it.    \n")
ShowTheDeck()
ShuffleTheDeck()
SectionTitle.write ("SHUFFLING...    \n")
Speaking.write ("Now, we show the shuffled cards below:   \n")
ShowTheDeck()
Speaking.write (f"Note the first and second cards in the deck are now the {mydeck._cards[0]} and {mydeck._cards[1]}.")
print()
SectionTitle.write("PART 3 - MOVE CARDS FROM THE DECK TO THE HAND    \n")
Speaking.write ("Step 3 instructs users on how to move objects from one place to another, and how to count the values being added. \nTo demonstrate, we will move two cards from the deck we just shuffled into the user's hand, and show the total value of the hand below each time.  \n")
MyDeal()
ShowMyHand()
Speaking.write ("and again:\n")
MyDeal()
ShowMyHand()
Speaking.write(f"To prove the card has been moved, here is the deck - the {myhand.cards[0]} and {myhand.cards[1]} have now gone! \n")
ShowTheDeck()
SectionTitle.write ("PART 4 - ADDING MORE HANDS TO DEAL TO    \n")
Speaking.write ("Lastly, we will create a second hand to deal to. Then, we'll deal two more cards from the deck to the other hand.    \n")
for i in (1,2):
    OtherDeal()
ShowOtherHand()
Speaking.write ("Because the deck has already dealt two cards to the user's hand, the hand still shows like show:")
ShowMyHand()
SectionTitle.write("This concludes the functionality presentation. Please press Enter to exit.")