from Deck import Deck
from Hand import Hand
from Game import Game

deck = Deck()
myHand = Hand(deck)
aiHand = Hand(deck)

myHand.drawHand()
aiHand.drawHand()

Game.startGame(deck, myHand, aiHand)
