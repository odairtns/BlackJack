class BetManagement():
    bet_amount = 0
    balance = 0

    def __init__ (self, balance):
        self.balance = balance
    
    def bet(self,amount):
        if(self.balance >= amount):
            self.bet_amount = amount
            print('Bet placed')
        else:
            print(f'Insuficient founts. Balance = {self.balance}')
    
    def win_bet(self):
        self.balance += self.bet_amount
        self.bet_amount = 0
    
    def lose_bet(self):
        self.balance -= self.bet_amount
        self.bet_amount = 0
        if self.balance == 0:
            print("No credits left")
        
    def draw_bet(self):
        self.balance = self.balance
        self.bet_amount = 0
        