from Card import Card

class Hand():
    def __init__(self, deck):
        self.deck = deck
        self.hand = []

    def drawHand(self):
        count = 1
        while count <= 7:
            self.hand.append(self.deck.drawCard())
            count += 1

    def getCardAt(self, number):
        return self.hand[number].get()
    
    def addCard(self):
        self.hand.append(self.deck.drawCard())

    def getLength(self):
        return len(self.hand)
    
    def playCard(self, number):
        del self.hand[number]

    def hasBook(self):
        var = 0
        cards = []
        while var < len(self.hand):
            cards.clear()
            temp = self.hand[var]
            cards.append(var)
            count = 0
            while count < len(self.hand):
                if count != var:
                    if temp.getNumber() == self.hand[count].getNumber():
                        cards.append(count)
                count += 1
                if (len(cards) == 4):
                    return cards
            var +=1
                
        return False
    
    def getHand(self):
        temp = ""
        count = 0
        while count < len(self.hand):
            temp += str(self.hand[count].getCard()) + " | "
            count += 1
        return temp
    
    def hasCardAt(self, card):
        count = 0
        while count < len(self.hand):
            if self.hand[count].getNumber() == card.getNumber():
                return count
            count += 1
        return -1

    def appendCard(self, card):
        self.hand.append(card)

    def giveCard(self, index):
        temp = self.hand[index]
        del self.hand[index]
        return temp