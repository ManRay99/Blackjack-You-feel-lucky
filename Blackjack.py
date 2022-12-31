import random
import math

cards = list (("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")) # define special cards

def drawcard():
    return random.randrange(13)

def getcardvalue(cardno):
    if cardno >= 9:
        return 10
    else:
        return cardno + 1

def main():
    input("welcome to blackjack, start new game?")
    card1 = drawcard()
    card2 = drawcard()
    print("You were dealt: " + cards[card1] + "," + cards[card2])
    cardtotal = getcardvalue(card1) + getcardvalue(card2)
    print ("Your total is: " + str(cardtotal))
    handfinished = False

    while handfinished == False:
        print("Would you like another card?")
        choice = input().lower()
        if choice == "y":
            newcard = drawcard()
            print("You were dealt: " + cards[newcard])
            cardtotal = cardtotal + getcardvalue(newcard)
            if cardtotal > 21:
                print("Your total is now " + str(cardtotal) + ", you are bust")
                handfinished = True
            else:
                print("Your total is now " + str(cardtotal))
        else:
            print("Your total was " + str(cardtotal))
            handfinished = True

main()