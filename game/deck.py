import random
from card import Card


class Deck:
    def __init__(self):
        ranks=Card.ranks
        suites=Card.suites
        deck=[]

        for rank in ranks:
            for suite in suites:
                card=Card(suite=suite, rank=rank)
                deck.append(card)
        self.deck=deck
    def shuffle():
        pass

    def remove_card():
        pass

    def add_to_end():
        pass
    
if __name__=="__main__":
    d1=Deck()