from Card import Card
import random

class Deck():
    deck = []
    count = 1
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    while count <= 4:
        deck.append(Card(1, " Ace of " + suits[count - 1]))
        countTwo = 2
        while countTwo <= 10:
            deck.append(Card(countTwo, " of " + suits[count - 1]))
            countTwo += 1
        deck.append(Card(11, " Jack of " + suits[count - 1]))
        deck.append(Card(12, " Queen of " + suits[count - 1]))
        deck.append(Card(13, " King of " + suits[count - 1]))
        count += 1
        
        temp = []
        while len(deck) >= 2:
            ran = random.randrange(0, (len(deck) - 1))
            temp.append(deck[ran])
            del deck[ran]
        temp.append(deck[0])
        del deck[0]
        deck = temp
    
    def drawCard(self):
        temp = self.deck[0]
        del self.deck[0]
        return temp
    
    def getLength(self):
        return len(self.deck)


