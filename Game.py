from Card import Card
import random

class Game():
    
    def startGame(deck, myHand, aiHand):
        deckCount = deck.getLength()
        myBooks = 0
        aiBooks = 0
        print("Welcome to Go Fish! Please note you and the computer will only gain books at the end of each turn.")
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
        choice = input("What will you ask for? Enter a number/Queen, jack, king, or ace\n")
        index = 0

        

        if choice == "Queen" or choice == "queen":
            choice = 12
            index = aiHand.hasCardAt(Card(int(choice), ""))
        elif choice == "Jack" or choice == "jack":
            choice = 11
            index = aiHand.hasCardAt(Card(int(choice), ""))
        elif choice == "King" or choice == "king":
            choice = 13
            index = aiHand.hasCardAt(Card(int(choice), ""))
        elif choice == "Ace" or choice == "ace":
            choice = 1
            index = aiHand.hasCardAt(Card(int(choice), ""))
        elif choice.isnumeric() == True:
            choice = int(choice)
            if choice > 0 and choice < 11:
                index = aiHand.hasCardAt(Card(int(choice), ""))
        else:
            print("That is not a valid option. Please try again.")
            return Game.myPlay(myHand, aiHand)


        if index >= 0:
            print("The computer had a " + str(choice) + " and gave you it")
            myHand.appendCard(aiHand.giveCard(index))
            return Game.myPlay(myHand, aiHand)
        else:
            print("Go fish!")
            print("You drew a card")
            myHand.addCard()
            if myHand.getCardAt(myHand.getLength() - 1).getNumber() == choice:
                print("You got the card you wanted so you can play again")
                return Game.myPlay(myHand, aiHand)
            


    def aiPlay(myHand, aiHand):
        aiChoices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        index = 0
        aiChoice = random.choice(aiChoices)

        if aiHand.hasCardAt(Card(aiChoice, "")) < 0:
            if aiHand.getLength() != 0:
                return Game.aiPlay(myHand, aiHand)


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
            return Game.aiPlay(myHand, aiHand)
        else:
            print("Go fish!")
            print("The computer drew a card")
            aiHand.addCard()
            if aiHand.getCardAt(aiHand.getLength() - 1).getNumber() == aiChoice:
                print("The computer got the card it wanted so it can play again")
                return Game.aiPlay(myHand, aiHand)

