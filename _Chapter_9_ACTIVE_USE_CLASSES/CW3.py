from CW2 import Card, Hand

class Deck(Hand):
    """Deck of gaming cards"""
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('Can\'t make cards more: cards over!')


if __name__ == '__main__':
    deck1 = Deck()
    print('Create new deck.')
    print('It\'s the deck')
    print(deck1)
    deck1.populate()
    print('\nIn deck appears new cards')
    print('Deck view now:')
    print(deck1)
    deck1.shuffle()
    print('\nDeck shuffle.')
    print('And now deck view:')
    print(deck1)

    my_hand = Hand()
    your_hand = Hand()
    hands = [my_hand, your_hand]
    deck1.deal(hands, per_hand = 5)
    print('\nMe and you gave on 5 cards')
    print('I have on hands: ')
    print(my_hand)
    print('Your hand:')
    print(your_hand)
    print('Remains in deck:')
    print(deck1)
    deck1.clear()
    print('\nDeck clear.')
    print('Deck now:')
    print(deck1)


