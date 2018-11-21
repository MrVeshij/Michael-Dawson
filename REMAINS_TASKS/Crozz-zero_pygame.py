FIELD = [0,1,2,3,4,5,6,7,8]
VICTORY_CELLS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
BEST_MOVES = (4,0,2,6,8,1,3,5,7)
TRICKY_MOVES = ((0,8),(2,6))
BUST_TRICK = 5
CHECK_LIST = ('0','1','2','3','4','5','6','7','8','9')

def intro():
    print(" The game with name Cross-Zero."
          "\n For victory obtain your symbol sequentially 3 cells.")


def print_field(field):
    """Print current field with all changes"""
    count = 0
    check = 0
    for i in field:
        count += 1
        check += 1
        if count < 3:
            if i in range(9):
                print('[ ', '_' , ' ]', end="")
            else: print('[ ', i, ' ]', end="")
        else:
            count = 0
            if i in range(9):
                print('[ ', '_', ' ]',end="")
            else: print('[ ', i, ' ]', end="")
            if check == 3:
                print('      ','[ ', 0, ' ]','[ ', 1, ' ]','[ ', 1, ' ]')
                print('---------------------       ----------------------')
            if check == 6:
                print('      ', '[ ', 3, ' ]', '[ ', 4, ' ]', '[ ', 5, ' ]')
                print('---------------------       ----------------------')
            if check == 9:
                print('      ', '[ ', 6, ' ]', '[ ', 7, ' ]', '[ ', 8, ' ]')
                print('---------------------       ----------------------')
            print('')


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
        move = input("Input number empty cage: \n")
        if move:
            for i in move:
                if i not in CHECK_LIST:
                    break
            else:
                move = int(move)
    return move


def move_comp(field, computer, human):
    """Return move computer"""
    for move in field:
        if move in FIELD:
            check_field = field[:]
            check_field[check_field.index(move)] = computer
            for row in VICTORY_CELLS:
                if check_field[row[0]] == check_field[row[1]] == check_field[row[2]] == computer:
                    return move
    for move in field:
        if move in FIELD:
            check_field = field[:]
            check_field[check_field.index(move)] = human
            for row in VICTORY_CELLS:
                if check_field[row[0]] == check_field[row[1]] == check_field[row[2]] == human:
                    return move
    for i in TRICKY_MOVES:
        if field[i[0]] == field[i[1]] == human:
            return BUST_TRICK
    for move in BEST_MOVES:
        if move in field:
            return move


def tie(field):
    """Check on tie"""
    for i in field:
        if i in range(9):
            return True
    return False


def congratulations(turn,field,human):
    """Check on conditions victory"""
    for i in VICTORY_CELLS:
        if field[i[0]] == field[i[1]] == field[i[2]] == turn:
            if turn == human:
                return 'Player won!'
            else:
                return 'Computer won!'


def game(field,human,computer,turn):
    """New controller of game|
    |Flexible version controller traceback who move and choose necessary player"""
    while tie(field):
        if turn == human:
            human_move = move_hum(field)
            field[field.index(human_move)] = human
        else:
            computer_move = move_comp(field,computer,human)
            field[field.index(computer_move)] = computer
            print_field(field)
        if congratulations(turn,field,human):
            print(congratulations(turn,field,human))
            break
        if turn == 'X': turn = 'O'
        else: turn = 'X'
    else:
        print('Tie!')


def main():
    """Main skeleton program"""
    intro()
    print()
    human, computer, turn = sign_hum()
    print(' Human - {} \n Computer - {}'.format(human, computer))
    if human == turn:
        print_field(FIELD)
    field = FIELD[:]
    game(field, human, computer, turn)
    print('Thanks for game, goodbye.')

main()