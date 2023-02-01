import random

class Card:

    #initalised with the card
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number
        if self._number in [str(n) for n in range (2,11)]:
            self.value = int(number)
        elif self._number in ["Jack","Queen","King"]:
            self.value = 10
        elif self.number in ["Ace"]:
            self.value = 1


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
        # print (self._cards)
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

mydeck = Deck()

# Printing original list
# print (mydeck._cards)
 
for i in range(len(mydeck._cards)-1, 0, -1):
     
    # Pick a random index from 0 to i
    j = random.randint(0, i + 1)
   
    # Swap arr[i] with the element at random index
    mydeck._cards[i], mydeck._cards[j] = mydeck._cards[j], mydeck._cards[i]
     
# Printing shuffled list
print ("The shuffled list is : " +  str(mydeck._cards)) 

class Hand:
    def __init__(self, handvalue):
        self.cards = []
        self.handvalue = handvalue

playerhand = Hand(0)
dealerhand = Hand(0)

takencard = mydeck._cards.pop (3)
print (takencard.value)


# mycard = Card("Spades","King")
# print (mycard)
# print (mycard.value)

