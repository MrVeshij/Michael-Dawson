# Написать игру крестики нолики
# Предлагаю ее сразу пульнуть через Tkinter

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
VICTORY_CELLS = ()


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
        return 'X'
    else:
        return 'O'


def sign_comp(human):
    """Return sign computer"""
    if human == 'X':
        return 'O'
    else:
        return 'X'


def move_hum(field):
    """Return move human"""
    move = None
    while move not in field:
        move = int(input("Input number empty cage: \n"))
    return move


def move_comp(field):
    """Return move computer"""
    for i in field:
        if i in range(9):
            print('test')
            print(i)
            return i
        #else:raise NameError('It\'s impossible')


def tie(field):
    for i in field:
        if i in range(9):
            return True
    return False


def game(field,human,computer):
    """Controller of game"""
    while tie(field):
        human_move = move_hum(field)
        field[field.index(human_move)] = human
        computer_move = move_comp(field)
        if computer_move or computer_move == 0:
            field[field.index(computer_move)] = computer
        print_field(field)




def main():
    """Main skeleton program"""
    intro()
    print()
    print_field(FIELD)
    human = sign_hum()
    computer = sign_comp(human)
    print(' Human - {} \n Computer - {}'.format(human, computer))
    field = FIELD[:]
    game(field, human, computer)
    print('Thanks for game, goodbye.')

main()