from Card import Card
import random

class Game():
    
    def startGame(deck, myHand, aiHand):
        deckCount = deck.getLength()
        myBooks = 0
        aiBooks = 0
        while deckCount > 1:
            print("________________________________________________________________________________")
            print("Your hand is")
            print(myHand.getHand())

            if aiHand.hasBook() != False:
                temp = aiHand.hasBook()
                print("The computer had a book")
                aiBooks += 1
                print("The computer now has " + str(aiBooks) + " books")
                aiHand.giveCard(temp[0])
                del temp[0]
                aiHand.giveCard(temp[0] - 1)
                del temp[0]
                aiHand.giveCard(temp[0] - 2)
                del temp[0]
                aiHand.giveCard(temp[0] - 3)
                del temp[0]

            if myHand.hasBook() != False:
                temp = myHand.hasBook()
                print("You have a book!")
                myBooks += 1
                print("You now have " + str(myBooks) + " books!")
                myHand.giveCard(temp[0])
                del temp[0]
                myHand.giveCard(temp[0] - 1)
                del temp[0]
                myHand.giveCard(temp[0] - 2)
                del temp[0]
                myHand.giveCard(temp[0] - 3)
                del temp[0]
                print("Your hand is now")
                print(myHand.getHand())

            Game.myPlay(myHand, aiHand)

            if myHand.hasBook() != False:
                temp = myHand.hasBook()
                print("You have a book!")
                myBooks += 1
                print("You now have " + str(myBooks) + " books!")
                myHand.giveCard(temp[0])
                del temp[0]
                myHand.giveCard(temp[0] - 1)
                del temp[0]
                myHand.giveCard(temp[0] - 2)
                del temp[0]
                myHand.giveCard(temp[0] - 3)
                del temp[0]
                print("Your hand is now")
                print(myHand.getHand())


            Game.aiPlay(myHand, aiHand)

            if aiHand.hasBook() != False:
                temp = aiHand.hasBook()
                print("The computer had a book")
                aiBooks += 1
                print("The computer now has " + str(aiBooks) + " books")
                aiHand.giveCard(temp[0])
                del temp[0]
                aiHand.giveCard(temp[0] - 1)
                del temp[0]
                aiHand.giveCard(temp[0] - 2)
                del temp[0]
                aiHand.giveCard(temp[0] - 3)
                del temp[0]


            deckCount = deck.getLength()
        if myBooks > aiBooks:
            print("You win!")
        elif aiBooks > myBooks:
            print("Computer wins")
        else:
            print("You and the computer tied!")

    def myPlay(myHand, aiHand):
        choice = input("What will you ask for? Enter a number/Queen, Jack, or King\n")
        index = 0
        if choice == "Queen":
            index = aiHand.hasCardAt(Card(12, ""))
        elif choice == "Jack":
            index = aiHand.hasCardAt(Card(11, ""))
        elif choice == "King":
            index = aiHand.hasCardAt(Card(13, ""))
        else:
            index = aiHand.hasCardAt(Card(int(choice), ""))


        if index >= 0:
            print("The computer had a " + str(choice) + " and gave you it")
            myHand.appendCard(aiHand.giveCard(index))
        else:
            print("Go fish!")
            print("You drew a card")
            myHand.addCard()
            


    def aiPlay(myHand, aiHand):
        aiChoices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        index = 0
        aiChoice = random.choice(aiChoices)
        if aiChoice == 11:
            print("The computer asked for a Jack")
            index = myHand.hasCardAt(Card(aiChoice, ""))
        elif aiChoice == 12:
            print("The computer asked for a Queen")
            index = myHand.hasCardAt(Card(aiChoice, ""))
        elif aiChoice == 13:
            print("The computer asked for a King")
            index = myHand.hasCardAt(Card(aiChoice, ""))
        else:
            print("The computer asked for a " + str(aiChoice))
            index = myHand.hasCardAt(Card(aiChoice, ""))

        if index >= 0:
            print("You gave the computer a card")
            aiHand.appendCard(myHand.giveCard(index))
        else:
            print("Go fish!")
            print("The computer drew a card")
            aiHand.addCard()

