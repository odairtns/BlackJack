import random 
class Deck():
    
    def __init__(self):
        self.deck = []
        self.card = ()
        self.ranks = ['A','1','2','3','4','5','6','7','8','9','J','Q','K']
        self.suits = {'spades':'♠','hearts':'♥','diamonds':'♦','clubs':'♣'}
        
    def __str__ (self):    
        return str(self.deck).strip('[]')     
    
    def __len__ (self):
        return len(self.deck)     
    
    def new_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append((rank,suit))
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def pick_top_card(self):
        try:
            return self.deck.pop(0)
        except:
            new_deck()
            random.shuffle(self.deck)
            return self.deck.pop(0)
            
    
    def pick_botton_card(self):
        try:
            return self.deck.pop(-1)    
        except:
            new_deck()
            random.shuffle(self.deck)
            return self.deck.pop(-1)
        
    def pick_card(self,position):
        if(type(position) == int):
            if (position - 1 <= len(self.deck) and position > 0):
                return self.deck.pop(position-1)
            else:
                print(f"Card not available.\nDeck has {len(self.deck)} cards.")
        else:
            print(f"Choose a valid position")    

    def print_card(self,card):                   
        print('┌───────┐')
        print(f'| {card[0]:<2}    |')
        print('|       |')
        print(f'|   {self.suits[card[1]]}   |')
        print('|       |')
        print(f'|    {card[0]:>2} |')
        print('└───────┘')        
        
    def print_cards(self,cards):
        num = len(cards)
        if(num == 1 or type(cards) == tuple):
            self.print_card(cards)
        else:
            l1,l2,l3,l4,l5,l6,l7 = '','','','','','',''
            for card in cards:
                l1 += '┌───────┐'
                l2 += f'| {card[0]:<2}    |'
                l3 += '|       |'
                l4 += f'|   {self.suits[card[1]]}   |'
                l5 += '|       |'
                l6 += f'|    {card[0]:>2} |'
                l7 += '└───────┘'
            print(l1)
            print(l2)
            print(l3)
            print(l4)
            print(l5)
            print(l6)
            print(l7)        
			
class BetManagement():        

    def __init__ (self, balance = 0):
        try:
            self.balance = float(balance)                            
        except:
            self.balance = 0
        self.bet_amount = 0
    
    def bet(self,amount):
        try:            
            if(self.balance >= amount):
                self.bet_amount = amount
                print('Bet placed')
                return True
            else:
                print(f'Insuficient founts. Balance = {self.balance}')
                return False
        except:
            return False
    
    def win_bet(self):
        self.balance += self.bet_amount
        self.bet_amount = 0
        print("You won the hand")
    
    def lose_bet(self):
        self.balance -= self.bet_amount
        self.bet_amount = 0
        print("You lost the hand")
        if self.balance == 0:
            print("No credits left")
        
    def draw_bet(self):
        self.balance = self.balance
        self.bet_amount = 0
        print("Draw")
        
class Player():

    def __init__ (self):
        self.__value = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':10,'Q':10,'K':10}
        self.__player_hand = []
        self.__ace = []
    
    def __str__ (self):
        return str(self.__player_hand).strip("[]")
    
    def add_card(self,card):
        self.__player_hand.append(card)
        
    def clear_hand(self):
        self.__player_hand.clear()
        self.__ace.clear()
    
    def hand(self):
        return self.__player_hand
    
    def hand_total(self):
        total_A = 0
        total_B = 0
        first_ace = False
        for card in self.__player_hand:
            if(card[0]=="A"):
                if(not first_ace):
                    total_A += 1
                    total_B += 11
                    first_ace = True
                else:
                    total_A += 1
                    total_B += 1
            else:       
                total_A += self.__value[card[0]]
                total_B += self.__value[card[0]]
        return (total_A,total_B)
    
    def print_hand_total(self):
        hand = self.hand_total()
        if(hand[0]==hand[1]):
            return hand[0]
        elif(hand[0]> 21 and hand[1]<=21):
            return hand[1]
        elif(hand[1]> 21 and hand[0]<=21):
            return hand[0]    
        elif(hand[0]> 21 and hand[1]>21):
            return min(hand)
        else:
            return hand

from IPython.display import clear_output

def BlackJack():
    '''
    Start Game
    '''
    deck = Deck()
    player = Player()
    dealer = Player()
    print("Welcome to Backjack Game!")
    initial_gamble = input("How much dou you want to gamble?")
    gamble_control = BetManagement(initial_gamble)
    deck.new_deck()
    deck.shuffle_deck()
    clear_output(wait=True)
    
    #Start of a new hand
    while True:
        '''
        Set gamble amount
        '''
        
        while True:
            bet_amount = gamble_control.bet(float(input("Place a bet: \n")))
            if bet_amount:
                break
            else:
                pass            

        '''
        Initiate hand
        '''
        player.clear_hand()
        dealer.clear_hand()
        has_winner = False
        player.add_card(deck.pick_top_card())
        player.add_card(deck.pick_top_card())
        dealer.add_card(deck.pick_top_card())
        dealer.add_card(deck.pick_top_card())

        #Initiate player hand
        while True:
            clear_output(wait=True)
            print(f"Initial balance = {gamble_control.balance}")            
            print(f"Bet amount = {gamble_control.bet_amount}\n")
            player_hand = player.hand_total()
            print("Dealer hand:")
            deck.print_cards(dealer.hand()[0])
            print("Player hand:")
            deck.print_cards(player.hand())
            print(f"Total amount = {player.print_hand_total()}")
            if(player_hand[0]== 21 or player_hand[1]== 21):
                dealer_hand = dealer.hand_total()
                if(dealer_hand[0]== 21 or dealer_hand[1]== 21):
                    has_winner = True
                    gamble_control.draw_bet()
                else:
                    gamble_control.win_bet()
                    has_winner = True
                break
            elif(player_hand[0]> 21 and player_hand[1]> 21):
                gamble_control.lose_bet() 
                has_winner = True
                break
            else:
                choice = input("Type 'h' to hit. Type any other to stop. ").lower()
                if(choice == 'h'):
                    player.add_card(deck.pick_top_card())
                else:
                    break   

        #initiate dealer hand          
        if not has_winner:                  
            while True:                  
                clear_output(wait=True)
                dealer_hand = dealer.hand_total()
                print("Dealer hand:")
                deck.print_cards(dealer.hand())
                print(f"Dealer Total Hand = {dealer.print_hand_total()}")                        
                print("Player hand:")
                deck.print_cards(player.hand())
                print(f"Player Total Hand = {player.print_hand_total()}\n\n")                                         
                if(dealer_hand[0]== 21 or dealer_hand[1]== 21):
                    gamble_control.lose_bet()           
                    break
                elif(dealer_hand[0]> 21 and dealer_hand[1]> 21):
                    gamble_control.win_bet()    
                    break
                elif((dealer_hand[0]> player_hand[0] and dealer_hand[0]> player_hand[1] and dealer_hand[0] <=21) or 
                (dealer_hand[1]> player_hand[0] and dealer_hand[1]> player_hand[1] and dealer_hand[1] <=21)):
                    gamble_control.lose_bet()    
                    break
                else:
                    dealer.add_card(deck.pick_top_card())    

        #Hand Result    
        print(f"\nYour balance is: {gamble_control.balance}")
        continue_playing = input("Press 'y' to keep playing.").lower()
        clear_output(wait=True)
        if(continue_playing == 'y'):
            if(gamble_control.balance == 0):
                print("You have insuficient founds.")
                initial_gamble = input("How much do you want to add?")
                gamble_control = BetManagement(float(initial_gamble))
            else:
                pass        
        else:
            clear_output(wait=True)
            print(f"You cashed out {gamble_control.balance}.")
            print("Thank you for playing. See you next time.")
            break 
			