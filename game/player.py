class Player:
    def __init__(self,name:str, money:int = 2000):
        self.name=name
        self.money=money
        self.cards=[]
        self.total_bet=0
        self.current_bet=0
    
    def bet(self, amount:int):
        pass
    
    def reset_bet(self):
        pass

    def __repr__(self):
        pass