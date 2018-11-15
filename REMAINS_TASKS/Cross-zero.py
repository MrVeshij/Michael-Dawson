# Написать игру крестики нолики
# Предлагаю ее сразу пульнуть через Tkinter
# Я написал код который уже дает какое то подобие игры, но нет контроля кто начинает ходить, я реалзиовал жесткий цикл
# с условием, что первым всегда ходит игрок. Теперь надо реализовать смену хода.


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


def move_comp(field):
    """Return move computer"""
    #Осталось добить логику компа и конец!
    for i in field:
        if i in range(9):
            return i


def tie(field,turn):
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
            return 'Victory' + turn + '!'


def game(field,human,computer,turn):
    """New controller of game|Гибкая версия контролера отслеживающая кто ходит и подставляя необходимого игрока
    |Flexible version controller traceback who move and choose necessary player"""
    while tie(field,turn):
        if turn == human:
            human_move = move_hum(field)
            field[field.index(human_move)] = human
        else:
            computer_move = move_comp(field)
            if computer_move or computer_move == 0:
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