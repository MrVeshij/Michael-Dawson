# 2)Напишите однокарточную версию игры «Война», структура раунда в которой такова: все игроки тянут по одной
# карте, а выигрывает тот, у кого номинал карты оказывается наибольшим.

# Псевдокод:
# Задается количество игроков
# Каждому игроку раздается по одной карте из колоды
# Показывается номинал карты вместе с именем игрока
# Выигрывает игрок с картой максимальной ценности, туз стоит 11 баллов

#Объекты игры "Война":
# Используем класс deck для составления колоды
# Создаем новый класс CardWar
# - добавляем метод value для определения стоимости карты находящийся в руке
# - создаем атрибут ценности туза равной 11 баллов
# Класс Hand исользуется для создания игроков
# Создаем класс Player
# - добавляем в метод конструктора атрибут name для определения игрока
#
# Создаем новый класс Game в котором прописываем логику игры и атрибуты включающие в себя созданные классы


import cards, games



class DeckWar(cards.Deck):
    def populate(self):
        for suit in CardWar.SUITS:
            for rank in CardWar.RANKS:
                self.add(CardWar(rank, suit))



class CardWar(cards.Card):
    """Player"""
    @property
    def value(self):
        """Defined value card"""
        v = self.RANKS.index(self.rank) + 1
        if v > 10:
            v = 10
        if v == 1:
            v = 11
        return v



class Player(cards.Hand):
    def __init__(self, name):
        """Add class Player attribute name"""
        super(Player, self).__init__()
        self.name = name



class Game():
    def __init__(self):
        """Create deck, list of names players, and list of players"""
        self.deck = DeckWar()
        self.names = []
        self.players = []

    def clear_all(self):
        """Clear all saves for last game"""
        for player in self.players:
            player.clear()
        self.names = []
        self.players = []
        self.deck.clear()

    def winner(self, players):
        """Defined who winner"""
        # список чисел , большее число выигрывает , функция макс - не подойдет если будут 2 карты с максимум баллов
        # нужно выявить самые большие числа и если есть такие же у других игроков вывести их победителями
        #TEST
        list_numb = []
        winners = []
        for player in players:
            list_numb.append(player.cards[0].value)
        max_numb = max(list_numb)
        for player in players:
            if player.cards[0].value == max_numb:
                winners.append(player)
        return winners


    def play(self):
        """Main method for start game"""
        self.deck.populate()
        self.deck.shuffle()
        numb = games.ask_number('How much player will play? (1-8)', 1, 9)
        for bymer in range(numb):
            name = input('Input name player:\n')
            self.names.append(name)
        for bymer in self.names:
            self.players.append(Player(bymer))
        self.deck.deal(self.players)
        for player in self.players:
            print(player.name, 'have card', player.cards[0], 'with cost', player.cards[0].value)
        winners = self.winner(self.players)
        print('\n\nOurs winners:')
        for winner in winners:
            print('Winner', winner.name)
        self.clear_all()



def main():
    game = Game()
    response = None
    while response != 'n':
        game.play()
        response = games.ask_yes_no('\nWill play again?\n\n')
    input('Press Enter for exit.')

main()

