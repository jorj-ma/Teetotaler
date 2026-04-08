class Card:
    suites = ["HEARTS", "DIAMONDS", "CLUBS", "SPADES"]
    ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, suite, rank):

        if not isinstance(suite, str):
            raise TypeError (f"suit expected to be a string got {type(suite).__name__}")
        
        if not isinstance(rank, str):
            raise TypeError(f"suit expected to be a string got {type(rank).__name__}")

        suite_upper=suite.upper()
        rank_upper=rank.upper()

        if rank_upper in Card.ranks:
            pass
        else:
            raise TypeError(f"Added rank not in rank list {ranks}")
        
        if suite_upper in Card.suites:
            pass
        else:
            raise TypeError(f"Added suit not in suit list {suites}")
        

        self.rank= rank_upper
        self.suite=suite_upper

    def print_card(self):
        print("Rank:",self.rank)
        print("Suite:",self.suite)

if __name__=="__main__":


    card2=Card(suite="Clubs", rank="3")
    card2.print_card()