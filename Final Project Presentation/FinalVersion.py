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


print ("\nPART 1 - GIVING THE CARDS VALUE")
print()
mycard = Card("Spades", "Ace")
print (mycard)
print (mycard._value)
print()
mycard2 = Card("Hearts", "Queen")
print (mycard2)
print (mycard2._value)
print()
print ("PART 2 - SHUFFLING THE DECK")
print()
ShowTheDeck()
ShuffleTheDeck()
print ("SHUFFLING...    \n")
ShowTheDeck()
print()
print("PART 3 - MOVE CARDS FROM THE DECK TO THE HAND    \n")
print("Let's move the first card in the deck to the hand \n")
MyDeal()
ShowMyHand()
print("To prove the card has been moved, here is the deck - notice the first card has now gone! \n")
ShowTheDeck()
print()
print("PART 4 - ADDING MORE HANDS TO DEAL TO    \n")
print ("Lastly, we will create a second hand to deal to. Then, we'll take add one more card to our hand, and deal two to the other hand.    \n")#     MyDeal()
MyDeal()
ShowMyHand()
for i in (1,2):
    OtherDeal()
ShowOtherHand()