import random 
class Deck():
    card = ()
    ranks = ['A','1','2','3','4','5','6','7','8','9','J','Q','K']
    suits = {'spades':'♠','hearts':'♥','diamonds':'♦','clubs':'♣'}
    
    def __init__(self):
        self.deck = []
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
        return self.deck.pop(0)
    
    def pick_botton_card(self):
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
        
   # def print_aligned_card(self,cards):                   
        #print(f'┌───────┐\n| {card[0]:<2}    |\n|       |\n|   {self.suits[card[1]]}   |\n|       |\n|    {card[0]:>2} |\n└───────┘')
        #for card in cards:            
      #  print(f'┌───────┐\n| {card[0]:<2}    |\n|       |\n|   {self.suits[card[1]]}   |\n|       |\n|    {card[0]:>2} |\n└───────┘')
        #    b.join(a,' ')            
       # print(b)