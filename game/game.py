from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.main_pot=0
        self.current_pot=0
        deck=Deck()
        deck.shuffle()
        human_cards=[deck.give_card(),deck.give_card()]
        pc_card=[deck.give_card(),deck.give_card()]
        
        self.human=Player(
            type="human",
            cards=human_cards,
            total_amount_bet=0,
            name="John",
            amount=2000
        )

        self.pc=Player(
            type="human",
            cards=human_cards,
            total_amount_bet=0,
            name="John",
            amount=2000
        )

        self.deck=deck

if __name__=="__main__":
    game=Game()
    game.deck.print_deck()
    print("This is the deck")
    print("PC cards")
    game.pc.cards[0].print_card()
    game.pc.cards[1].print_card()
    print("This is the deck")
    print("Humaan cards")
    game.human.cards[0].print_card()
    game.human.cards[1].print_card()