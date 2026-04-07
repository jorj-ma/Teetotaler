from .deck import Deck
from .player import Player
from .moves import Moves


class Game:
    def __init__(self, human_name="Taler", comp_name="Max"):
        self.deck = Deck()
        self.deck.shuffle()
        self.pot = 0
        self.round = 1
        self.players = [Player(human_name), Player(comp_name)]
        self.community_cards = []

    def betting_round(self):
        pass

    def start(self):
        pass

    def deal_community_cards(self, num):
        pass

    def determine_winner(self):
        pass

    def reset_round(self):
        pass
