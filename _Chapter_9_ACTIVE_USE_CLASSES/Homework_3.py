# 3)Доработайте проект «Блек-джек» так, чтобы игроки могли делать ставки. Программа должна следить за капи­
# талом каждого игрока и выводить из-за стола тех, у кого закончатся деньги.

#!!!!! Ввел в игру дополнительный атрибут кошелька, и условие, что при его значение 0 игрок вылетает из игры
# ДОДЕЛАТЬ - Ввести возможность устанавливать ставки при каждой новой итерации, если игрок выигрывает
# дилер дает ему двойной выгрыш, если прогрывает деньги теряются.
# Подумать имеет ли смысл вводить дилеру деньги? Или сделать перемещения денег не зависимым от дилера.

# Description:
# Модифицируем класс BG_Player - добавляем в него новое значение кошелек с некой суммой
# - Добавляем метод на передачу денег
# У дилера кошелек безграничный
# У игроков сумма равняется 1000
# Блок логики взаимодействия описываем в теле класса BJ_Game
# Каждая игра стоит 100 монет
# При проигрыше - деньги передаются дилеру
# Сумма выигрыша суммируется вплоть до прогрыша последнего участника.
# При проигрыше дилера, каждому оставшиемуся участнику дают удвоенную сумму

# Для начала реализовать возможность просто получения/трат денег в каждой игре - потом реализовать возможность
# делать ставки

# Псевдокод:
# BJ_Player - аттрибут wallet по умолчанию при создания объекта класса равный 1000
# - метод transfer передающий n монет n участнику игры
#
#
# BJ_Dealer - аттрибут wallet равный 100000
# - добавить наследование от BJ_Player

import cards, games


class BJ_Card(cards.Card):
    """Card for game Black Jack"""
    ACE_VALUE = 1
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v



class BJ_Deck(cards.Deck):
    """Deck for game in Black Jack"""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

    def check_lot(self):
        if len(self.cards) < 32:
            self.cards = []
            self.populate()
            self.shuffle()
            print('Deck shuffled include dump.')




class BJ_Hand(cards.Hand):
    """Hand: set cards of Black Jack by one player"""
    def __init__(self, name, bet = 100, wallet = 1000):
        super(BJ_Hand, self).__init__()
        self.name = name
        self.wallet = wallet
        self.bet = bet

    def __str__(self):
        rep = self.name + ':\t' + super(BJ_Hand, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        return rep

    @property
    def total(self):
        """If one card value equal None, all property equal None"""
        for card in self.cards:
            if not card.value:
                return 0
        t = 0
        for card in self.cards:
            t += card.value
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        if contains_ace and t <= 11:
            t += 10
        return t


    def is_busted(self):
        return self.total > 21



class BJ_Player(BJ_Hand):
    """Player in Black Jack"""
    def __init__(self, name, dealer):
        super().__init__(name)
        self.dealer = dealer

    def is_hitting(self):
        response = games.ask_yes_no('\n' + self.name + ', Will you more cards? (Y/N): ')
        return response == 'y'

    def bust(self):
        print(self.name, 'bust.')
        self.lose()

    def lose(self):
        print(self.name, 'lose.')
        self.wallet -= self.bet
        print('Wallet player equal:', self.wallet)
        self.dealer.wallet += self.bet
        print('Dealer comer some rich.\tHis wallet equal {}.'.format(self.dealer.wallet))
        print()
        if self.wallet <= 0:
            print('Player lost all money, he went away.')

    def win(self):
        print(self.name, 'win.')
        self.wallet += self.bet
        print('Wallet player equal:', self.wallet)
        self.dealer.wallet -= self.bet
        print('You get money from dealer.\tDealer remains with {}.'.format(self.dealer.wallet))
        print()

    def push(self):
        print(self.name, 'played with dealer in tie.')
        print()



class BJ_Dealer(BJ_Hand):
    """Dealer in game Black-Jack"""
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, 'bust.')
        print()

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()



class BJ_Game():
    """Game in Black Jack"""
    def __init__(self, names):
        self.players = []
        self.dealer = BJ_Dealer('Dealer', wallet = 10000)
        for name in names:
            player = BJ_Player(name,dealer = self.dealer)
            self.players.append(player)
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.bankrupt = 0
        self.shutdown = 0

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp


    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def check_bet(self,player):
        player.bet = input('{} input your bet for that round.\n'.format(player.name))
        while not games.check_number(player.bet) or not player.bet:
            player.bet = input('Input number.\n\n')
        player.bet = int(player.bet)


    def play(self):
        print('You begun played in BJ with wallet equal 1000 dollars.\n')
        for player in self.players:
            if not player.wallet <= 0:
                self.check_bet(player)
                while True:
                    if not 0 <= player.bet <= player.wallet:
                        print('You input incorrect sum. Input correct.\n')
                        self.check_bet(player)
                    else:
                        break
            else:
                self.players.remove(player)
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player,end='\t')
            print('Wallet equal: {} \t Bet equal: {}'.format(player.wallet,player.bet))
        print('\n',self.dealer,sep='')
        print('Dealer wallet equal:', self.dealer.wallet)
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()
        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                print()
                for player in self.still_playing:
                    player.win()
            else:
                print()
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        for player in self.players:
            self.bankrupt += player.wallet
        if self.bankrupt == 0:
            print('\nGame over. All players are bankrupts.')
            self.shutdown = 1
        else:
            self.bankrupt = 0
        if self.dealer.wallet <= 0:
            print('Dealer cry call some guys with guns. Casino closed...')
            self.shutdown = 1
        self.dealer.clear()
        self.deck.check_lot()



def main():
    print('\t\tWelcome to game table Black Jack!\n')
    names = []
    number = games.ask_number('How much players? (1-7): ', low = 1, high = 8)
    for i in range(number):
        name = input('Input name player:\n')
        while not name:
            name = input('Input name player:\n')
        names.append(name)
        print()
    game = BJ_Game(names)
    again = None
    while again != 'n':
        game.play()
        if game.shutdown == 1: break
        again = games.ask_yes_no('\nWould you play again?')
    input('\n\nPress Enter for exit.')

main()
