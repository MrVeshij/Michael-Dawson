# Написать игру крестики нолики
# Предлагаю ее сразу пульнуть через Tkinter
# Я написал код который уже дает какое то подобие игры, но нет контроля кто начинает ходить, я реалзиовал жесткий цикл
# с условием, что первым всегда ходит игрок. Теперь надо реализовать смену хода.
# Реализовать версию крестики нолики через Pygame
# После написания версии на tkintere проверить книжный код на корректность и необходимость последнего этапа проверки
# На упущенную победу


def description():
    """
    Псевдо-код:
    На экран выводится описание игры.
    Пользователь выбирает X или O.
    При выборе О, ПК ставит крестик в центр игрового поля, при выборе Х игрок выбирает поле куда ставить Х.
    Игра заканчивает когда не остается свободных полей либо 3 ячейки по диагонали/вертикали/горизонтали имеют одинаковый знак
    После завершении игры выводится победитель и предложение повторить игру

    global_values:
    - Поле
    - Победные комбинации

    func's:
    - intro (Описывает игровой процесс)
    - printfield(отрисовывает текущее поле)
    - choose_mark( выбор для пользователя)
    - kontroller ( контроль процесса игры, подменят отметку при передаче хода, организует передачу хода)
    - who_win ( проверка на победителя)
    - finish_letter ( пишет победителя)
    """
    pass

#Global values
FIELD = [0,1,2,3,4,5,6,7,8]
VICTORY_CELLS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
BEST_MOVES = (4,0,2,6,8,1,3,5,7)
TRICKY_MOVES = ((0,8),(2,6))
BUST_TRICK = 5

def intro():
    print(" Эта игра под названием крестики-нолики.\n Для победы займите своим символом последовательно 3 ячейки.")

def print_field(field):
    """Рисует текущее игровое поле"""
    count = 0
    for i in field:
        count += 1
        if count < 3:
            print('[ ', i , ' ]', end="")
        else:
            count = 0
            print('[ ', i, ' ]')
            print('---------------------')


def sign_hum():
    """Return sign player"""
    mark = ''
    while mark != 'y' and mark != 'n':
        mark = input('You want play first?(y/n)').lower()
    if mark == 'y':
        return 'X','O','X'
    else:
        return 'O','X','X'


def move_hum(field):
    """Return move human"""
    move = None
    while move not in field:
        move = int(input("Input number empty cage: \n"))
    return move


def move_comp(field, computer, human): # Атрибут* turn применяется только в случае хода компьютера когда его фишка и фишка хода совпадает
    """Return move computer"""
    #Осталось добить логику компа и конец!
    #Проверка на хитрого юзера
    #Проверка на упускание победы
    for move in field: # Проверка на победителя ии
        if move in FIELD: # Проверка на пустую ячейку
            check_field = field[:]
            check_field[check_field.index(move)] = computer
            for row in VICTORY_CELLS:
                if check_field[row[0]] == check_field[row[1]] == check_field[row[2]] == computer:
                    return move
    for move in field: # Проверка на опережения хода игрока
        if move in FIELD:
            check_field = field[:]
            check_field[check_field.index(move)] = human
            for row in VICTORY_CELLS:
                if check_field[row[0]] == check_field[row[1]] == check_field[row[2]] == human:
                    return move
    # Check tricky user | Проверяет на угловую стратегию
    for i in TRICKY_MOVES:
        if field[i[0]] == field[i[1]] == human:
            return BUST_TRICK
    # Проверка на лучшие ходы
    for move in BEST_MOVES:
        if move in field:
            return move


def tie(field):
    """Check on tie"""
    #Проверяет на заполненнсоть поля
    for i in field:
        if i in range(9):
            return True
    return False


def congratulations(turn,field):
    """Проверяет на условие победы партии|Check on conditions victory"""
    for i in VICTORY_CELLS:
        if field[i[0]] == field[i[1]] == field[i[2]] == turn:
            return 'Victory ' + turn + '!'


def game(field,human,computer,turn):
    """New controller of game|Гибкая версия контролера отслеживающая кто ходит и подставляя необходимого игрока
    |Flexible version controller traceback who move and choose necessary player"""
    while tie(field):
        if turn == human:
            human_move = move_hum(field)
            field[field.index(human_move)] = human
        else:
            computer_move = move_comp(field,computer,human)
            if computer_move or computer_move == 0: # Защита от 10 пустого хода компьютером
                field[field.index(computer_move)] = computer
            print_field(field)
        if congratulations(turn,field):
            print(congratulations(turn,field))
            break
        if turn == 'X': turn = 'O'
        else: turn = 'X'
    else:
        print('Tie!')


def main():
    """Main skeleton program"""
    intro()
    print()
    print_field(FIELD)
    human, computer, turn = sign_hum()
    print(' Human - {} \n Computer - {}'.format(human, computer))
    field = FIELD[:]
    game(field, human, computer, turn)
    print('Thanks for game, goodbye.')

main()