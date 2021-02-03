import DeckManagement as dm
from BetManagement import BetManagement as bm

deck = dm.Deck()
deck.new_deck()
deck.shuffle_deck()
card = deck.pick_top_card()
deck.print_card(card)
table = bm.BetManagement(500)
print(table.balance)