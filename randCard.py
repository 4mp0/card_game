
import pygame
import random as rand

class randCard:
    def __init__(self, cards: list[str]):
        self.cards = []
        self.cards.append(cards[0])
        self.cards.append(cards[1])
        self.cards.append(cards[2])
    def rand(self):
        self.randNumb = rand.Random.randint( 0, len(self.cards))
        self.randCard = self.cards
        return self.cards