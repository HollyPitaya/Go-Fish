class Card():
    
    def __init__(self, number, theType):
        self.number = number
        self.theType = theType

    def getCard(self):
        if self.number >= 11 or self.number == 1:
            return self.theType
        return str(self.number) + self.theType
    
    def getNumber(self):
        return self.number
    
    def getType(self):
        return self.theType
    
    def get(self):
        return self


