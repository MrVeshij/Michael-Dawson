import cards, games


class BJ_Card(cards.Card):
    """Card for game Black Jack"""
    ACE_VALUE = 1 # Ценность туза == 1
    @property
    def value(self): # Стоимость карты
        if self.is_face_up: # Если карта открыта выполняет нижеуказанную логику
            v = BJ_Card.RANKS.index(self.rank) + 1 # метод принимает в себя число которое эта карта занимает в списке + 1
            if v > 10: # Все карты выше 10 делает по стоимости равным 10
                v = 10 #!!!! Здесь была заключена ошибка - неправильно были размещены блоки логики, было следующее - если v был меньше 10 его значение становилось равным 10
        else:
            v = None
        return v



class BJ_Deck(cards.Deck):
    """Deck for game in Black Jack"""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))



class BJ_Hand(cards.Hand):
    """Hand: set cards of Black Jack by one player"""
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ':\t' + super(BJ_Hand, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        return rep

    @property # свойство - переделывают функцию в атрибут, теперь для ее вызова нет необходимости указывать скобки
    def total(self): # Функция подсчета очков стоимости карт
        """If one card value equal None, all property equal None"""
        for card in self.cards: # Список Player в котором содеражатся карты объекты - перебор спсика
            if not card.value: # Если карта закрыта
                return 0 # Возвращает стоимость 0
        t = 0
        for card in self.cards: #Перебор списка
            t += card.value # Конкатенация ценности карт
        contains_ace = False #Проверка на туза
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE: #Разобрать логику работы с тузом
                contains_ace = True # Если туз есть в колоде , значение равно True
        if contains_ace and t <= 11: # Если есть туз и общий пул очков меньше или равно 11
            t += 10 # Суммирует 10 очков
        return t

    def is_busted(self):
        return self.total > 21



class BJ_Player(BJ_Hand):
    """Player in Black Jack"""
    def is_hitting(self):
        response = games.ask_yes_no('\n' + self.name + ', Will you more cards? (Y/N): ')
        return response == 'y'  #Возвращает True или False в зависимости от ввода игрока

    def bust(self):
        print(self.name, 'bust.')
        self.lose()

    def lose(self):
        print(self.name, 'lose.')

    def win(self):
        print(self.name, 'win.')

    def push(self):
        print(self.name, 'played with computer in tie.')



class BJ_Dealer(BJ_Hand):
    """Dealer in game Black-Jack"""
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, 'bust.')

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()



class BJ_Game():
    """Game in Black Jack"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer('Dealer')
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()


    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp


    def __additional_cards(self, player): #Метод добавления новых карт в руку игрока при условии:
        while not player.is_busted() and player.is_hitting(): # Что Игрок не набрал очков больше 21 и не отказался от добора
            self.deck.deal([player]) # метод deal делает перебор списка, а так как player это не часть списка без заключения player в квадратные скобки - будет ошибка
           # deck это атрибут класса BJ_Game, которая взял в себя класс BJ_Deck у которого есть метод deal
            print(player) # Выводит представление обьекта класса Player, его карты
            if player.is_busted(): #!!! Если стоимость карт выше 21: (проверить каким образом обьект Player имеет значение value?)
                player.bust() # На экран выводится сообщение о переборе и последующем проигрыше


    def play(self):
        #Применяется объект класса BG_Deck который принимает список игроков и количество рук
        self.deck.deal(self.players + [self.dealer], per_hand = 2) #Игроки включая дилера получают по 2 карте
        self.dealer.flip_first_card() #Экземпляр класса Card меняется на закрытй вид XX
        for player in self.players: #перебор списка с игроками
            print(player) # выводятся экземпляры классов через метод __str__ (из списка игроков)
        print(self.dealer) # выводится экземпляр класса через метод __str__
        for player in self.players: # Перебор списка с игроками
            self.__additional_cards(player) # Обращение к методу класа Game для добора карт в руку
            self.dealer.flip_first_card() # Раньше эта строка была смещена и участвовала в переборе списка, при четном количестве игроков, у дилера невозможно было установить ценость карт, что не ввело к перебору и впоследствии приводило к бесконечному циклу
        if not self.still_playing: #Проверяет список игроков, если игроки есть:
            print(self.dealer) # Выводит на экран свои статы через метод __str__
        else:
            print(self.dealer) # Иначе также выводит статы
            self.__additional_cards(self.dealer) # Добавляет дилеру карты пока он не настигнет значение выше 17
            if self.dealer.is_busted(): # Если дилер превысил стоимость колоды в 21 балл
                for player in self.still_playing: # Перебирает список оставшихся в игре игроков
                    player.win() # объявляет их победителями
            else:
                for player in self.still_playing: # Иначе для оставшихся игроков (Перебор списка)
                    if player.total > self.dealer.total: # Если игрок набрал больше - победа
                        player.win()
                    elif player.total < self.dealer.total: # Если игрок набрал меньше - проигрыш
                        player.lose()
                    else:
                        player.push() # При всех остальных случаях - ничья
        for player in self.players: # очистка рук игроков
            player.clear()
        self.dealer.clear() # Очистка руки дилера


def main():
    print('\t\tWelcome to game table Black Jack!\n')
    names = []
    number = games.ask_number('How much players? (1-7): ', low = 1, high = 8)
    for i in range(number):
        name = input('Input name player:\n')
        names.append(name)
        print()
    game = BJ_Game(names)
    again = None
    while again != 'n':
        game.play() #1 Запуск игры, точка отсчета
        again = games.ask_yes_no('\nWould you play again?')
    input('\n\nPress Enter for exit.')

main()
