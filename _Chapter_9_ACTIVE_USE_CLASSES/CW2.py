class Card():
    """One card game"""
    RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    SUITS = ['c','d','h','s']
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand():
    """Hand: set of cards on hands one player"""
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + ' '
        else:
            rep = '<empty>'
        return rep

    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)



if __name__ == '__main__':
    card1 = Card(rank = 'A', suit = 'c')
    print('Print on screen object-card:')
    print(card1)
    card2 = Card(rank = '2', suit = 'c')
    card3 = Card(rank = '3', suit = 'c')
    card4 = Card(rank = '4', suit = 'c')
    card5 = Card(rank = '5', suit = 'c')
    print('\nPrint else 4 cards:')
    print(card2)
    print(card3)
    print(card4)
    print(card5)

    my_hand = Hand()
    print('\nPrint cards, which i have on my hands before game:')
    print(my_hand)
    my_hand.add(card1)
    my_hand.add(card2)
    my_hand.add(card3)
    my_hand.add(card4)
    my_hand.add(card5)
    print('\nPrint 5 cards, which i have on my hands:')
    print(my_hand)

    your_hand = Hand()
    my_hand.give(card1, your_hand)
    my_hand.give(card2, your_hand)
    print('\nFirst two cards i gave you.')
    print('Now you have on hands:')
    print(your_hand)
    print('And i have:')
    print(my_hand)

    my_hand.clear()
    print('\nI have on my hands after their clear:')
    print(my_hand)
