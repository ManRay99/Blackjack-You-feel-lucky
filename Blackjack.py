import random
import math

cards = list (("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")) # define special cards

class HandCard:
    def __init__(self, cardnumber):
        self.cardnumber = cardnumber
        self.nextcard = None

class Hand:
    def __init__(self):
        self.firstcard = None

    def addcard(self, newcard: HandCard):
        lastcard = self.firstcard
        if self.firstcard == None:
            self.firstcard = newcard
            return
        while(lastcard.nextcard != None):
            lastcard = lastcard.nextcard
        lastcard.nextcard = newcard

def gethandvaluenoaces(currentcard: HandCard, handvalue):
    if currentcard.nextcard == None:
        if currentcard.cardnumber == 0:
            return handvalue
        elif currentcard.cardnumber >= 9:
            return handvalue + 10
        else:
            return handvalue + currentcard.cardnumber + 1
    
    if currentcard.cardnumber == 0:
        handvalue = gethandvaluenoaces(currentcard.nextcard, handvalue)
    elif currentcard.cardnumber >= 9:
        handvalue = gethandvaluenoaces(currentcard.nextcard, handvalue + 10)
    else:
        handvalue = gethandvaluenoaces(currentcard.nextcard, handvalue + currentcard.cardnumber + 1)
    
    return handvalue
    
def getnumberofaces(currentcard: HandCard, numberofaces):
    if currentcard.nextcard == None:
        if currentcard.cardnumber == 0:
            return numberofaces + 1
        else:
            return numberofaces

    if currentcard.cardnumber == 0:
        numberofaces = getnumberofaces(currentcard.nextcard, numberofaces + 1)
    else:
        numberofaces = getnumberofaces(currentcard.nextcard, numberofaces)

    return numberofaces
        
def gethandvaluewithaces(numberofaces, handvalue):
    if numberofaces == 0:
        return handvalue
    if (handvalue + 11 <= 21):
        handvalue = gethandvaluewithaces(numberofaces-1,handvalue+11)
    else:
        handvalue = gethandvaluewithaces(numberofaces-1,handvalue+1)

    return handvalue

def drawcard():
    return random.randrange(13)

def checkblackjack(card1, card2):
    if (card1 == 0 and card2 >= 9) or (card2 == 0 and card1 >= 9):
        return True
    else:
        return False

def weightedrandomgenerator(numberneeded, luckfactor, luckscalefactor, drawbustfactor):
    weightedlist = []
    if numberneeded > 9:
        numbersbelowcounter = 9
    else:
        numbersbelowcounter = numberneeded -1
    templuck = luckfactor * luckscalefactor
    while numbersbelowcounter > -1:
        weightedlist = weightedlist + [numbersbelowcounter] * math.floor(templuck)
        numbersbelowcounter = numbersbelowcounter - 1
        templuck = templuck * luckscalefactor
    if numberneeded > 9:
        numbersabovecounter = 13
    else:
        numbersabovecounter = numberneeded +1
    templuck = luckfactor * luckscalefactor * drawbustfactor
    while numbersabovecounter < 13:
        weightedlist = weightedlist + [numbersabovecounter] * math.floor(templuck)
        numbersabovecounter = numbersabovecounter + 1
        templuck = templuck * luckscalefactor * drawbustfactor
    if numberneeded > 9:
        numberneeded = 0
    weightedlist = weightedlist + [numberneeded] * luckfactor
    print(weightedlist)
    return random.choice(weightedlist)

def starthand():
    card1 = drawcard()
    card2 = drawcard()
    print("You were dealt: " + cards[card1] + "," + cards[card2])
    hand = Hand()
    hand.addcard(HandCard(card1))
    hand.addcard(HandCard(card2))
    noacevalue = gethandvaluenoaces(hand.firstcard, 0)
    acecount = getnumberofaces(hand.firstcard, 0)
    if acecount == 0:
        print ("Your total is: " + str(noacevalue))
    else:
        acevalue = gethandvaluewithaces(acecount, noacevalue)
        print ("Your total is: " + str(acevalue))
    handfinished = False
    cansplit = card1 == card2
    if checkblackjack(card1, card2):
        print("Blackjack!")
        handfinished = True

    while handfinished == False:
        print("what would you like to do?")
        choice = input().lower()
        if choice == "hit":
            newcard = drawcard()
            print("You were dealt: " + cards[newcard])
            hand.addcard(HandCard(newcard))
            noacevalue = gethandvaluenoaces(hand.firstcard, 0)
            acecount = getnumberofaces(hand.firstcard, 0)
            if acecount == 0:
                if noacevalue > 21:
                    print("Your total is now " + str(noacevalue) + ", you are bust")
                    handfinished = True
                elif noacevalue == 21:
                    print("Your total is now " + str(noacevalue) + ", you win!")
                    handfinished = True
                else:
                    print("Your total is now " + str(noacevalue))
            else:
                acevalue = gethandvaluewithaces(acecount, noacevalue)
                print ("Your total is: " + str(acevalue))
                if acevalue > 21:
                    print("Your total is now " + str(acevalue) + ", you are bust")
                    handfinished = True
                elif acevalue == 21:
                    print("Your total is now " + str(acevalue) + ", you win!")
                    handfinished = True
                else:
                    print("Your total is now " + str(acevalue))
        elif choice == "stand":
            if acecount == 0:
                print("Your total was " + str(noacevalue))
            else:
                print("Your total was " + str(acevalue))
            handfinished = True
        elif choice == "lucky":
            if acecount == 0:
                print(str(noacevalue))
                newcard = weightedrandomgenerator(21-noacevalue, 50, 0.75, 0.75)
            else:
                print(str(acevalue))
                newcard = weightedrandomgenerator(21-acevalue, 50, 0.75, 0.5)
            print("You were dealt: " + cards[newcard])
            hand.addcard(HandCard(newcard))
            noacevalue = gethandvaluenoaces(hand.firstcard, 0)
            acecount = getnumberofaces(hand.firstcard, 0)
            if acecount == 0:
                if noacevalue > 21:
                    print("Your total is now " + str(noacevalue) + ", you are bust")
                    handfinished = True
                elif noacevalue == 21:
                    print("Your total is now " + str(noacevalue) + ", you win!")
                    handfinished = True
                else:
                    print("Your total is now " + str(noacevalue))
            else:
                acevalue = gethandvaluewithaces(acecount, noacevalue)
                print ("Your total is: " + str(acevalue))
                if acevalue > 21:
                    print("Your total is now " + str(acevalue) + ", you are bust")
                    handfinished = True
                elif acevalue == 21:
                    print("Your total is now " + str(acevalue) + ", you win!")
                    handfinished = True
                else:
                    print("Your total is now " + str(acevalue))
        else:
            print("Not a valid action")

def aceunittest():
    acetesterhand = Hand()
    acetesterhand.firstcard = HandCard(0)
    acetesterhand.addcard(HandCard(0))
    testnoacevalue = gethandvaluenoaces(acetesterhand.firstcard, 0)
    testacecount = getnumberofaces(acetesterhand.firstcard, 0)
    testacevalue = gethandvaluewithaces(testacecount, testnoacevalue)
    print(str(testacevalue))

def main():
    
    print("Welcome to blackjack")
    isplaying = True
    while isplaying == True:
        print("Start new hand?")
        continuechoice = input().lower()
        if continuechoice == "y":
            print("New hand started")
            starthand()
        else:
            print("Goodbye!")
            isplaying = False
    
main()