from CW2 import Card

class Unprintable_Card(Card):
    """Card, rank, suit which cant print on screen"""
    def __str__(self):
        return "<Not print>"

class Positionable_Card(Card):
    """Card, which i lay face down or up"""
    def __init__(self, rank, suit, face_up = True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = 'XX'
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


if __name__ == '__main__':
    card1 = Card('A', 'c')
    card2 = Unprintable_Card('A', 'd')
    card3 = Positionable_Card('A', 'h')

    print('Print object Card:')
    print(card1)
    print('\nPrint object Unprintable_Card:')
    print(card2)
    print('\nPrint object Positionable_Card:')
    print(card3)
    print('Flip object Positionable_Card.')
    card3.flip()
    print('\nPrint object Positionable_Card.')
    print(card3)



