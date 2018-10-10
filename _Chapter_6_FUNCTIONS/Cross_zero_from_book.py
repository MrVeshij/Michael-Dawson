# Pseudo code
# вывести  на  экран  инструкции  для  игрока
# решить.  кому  принадлежит  первый  ход
# создать  пустую  доску  для  игры  в  "Крестики-нолики"
# отобразить  эту  доску
# до  тех  пор  пока  никто  не  выиграл  или  не  состоялась  ничья
# если  сейчас  ход  пользователя
# получить  ход  из  пользовательского  ввода
# изменить  вид  доски
# иначе
# рассчитать  ход  компьютера
# изменить  вид  доски
# вывести  на  экран  обновленный  вид  доски
# осуществить  переход  хода
# поздравить  победителя  или  констатировать  ничью

# Список
# display _instruct()
# Выводит инструкцию для игрока

# ask_yes_пo(question)
# Задает вопрос, ответом на который может быть «Да» или «Нет».
# Принимает текст вопроса, возвращает ''у"  или "п"

# ask_пumЬer(question, low,high)
# Просит ввести число из указанного диапазона. Принимает текст
# вопроса, нижнюю (low) и верхнюю (high) границы диапазона.
# Возвращает целое число не меньше low и не больше high

# pieces()
# Определяет принадлежность первого хода человеку или компьютеру.
# Возвращает типы фишек соответственно компьютера и человека

# пew_board()
# Создает пустую игровую досху. Возвращает эту доску

# display _board(board)
# Отображает игровую доску на экране. Принимает эту доску

# legal_moves(board)
# Создает список доступных ходов. Принимает доску. Возвращает список доступных ходов

# winner(board)
# Определяет победителя игры. Принимает доску. Возвращает тип фишек победителя: "Ничья• или None

# human_move(board, human)
# Узнает, какой ход желает совершить игрок. Принимает доску и тип фишек человека.
# Возвращает ход человека

# computer _move(board,computer,human) Рассчитывает ход компьютерного противника. Принимает доску,
# тип фишек компьютера и тип фишек человека. Возвращает ход компьютера

# next_tum(turn)
# Осуществляет переход к следующему ходу.
# Принимает тип фишек. Возвращает тип фишек

# congrat_winner(the_winner, computer, human)
# Поздравляет победителя или констатирует ничью. Принимает
# тип фишек победителя, тип фишек компьютера и тип фишек человека

#Global values
X = "X"
O = "O"
EMPTY = " "
TIE = 'TIE'
NUM_SQUARES = 9

def display_instruct():
    """Print instruction for player"""
    print(
        """
        Welcome to the game cross - zero.
        \n"""
    )

def ask_yes_no(question):
    """Ask question with answer 'yes' or 'no'"""
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Asks input number from range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Defined who make first turn"""
    go_first = ask_yes_no('Want you stay first turn? (y/n): ')
    if go_first == 'y':
        print('\nYou play cross')
        human, computer = X, O
        return human, computer
    else:
        print('I play with zero')
        human, computer = O, X
        return human, computer

def new_board():
    """Create new game board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """View game board an screen"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "--------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "--------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    """Create list available moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Defined winner in the game"""
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    """Get turn human"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Your turn.Choose one square (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square occupied. Choose another square")
    print("Ok")
    return move

def computer_move(board, computer, human):
    """Make turn for computer"""
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I choose square", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            return move
        board[move] = EMPTY
    # if board[8] == human:
    #     move = 2
    #     return move
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Make transfer turn"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Congratulations winner the game!"""
    if the_winner != TIE:
        print("Three", the_winner, "in line!\n")
    else:
        print('Tie!\n')
    if the_winner == computer:
        print('Computer win.')
    elif the_winner == human:
        print('Human win')
    elif the_winner == TIE:
        print('Nobody wins')

def main():
    display_instruct()
    human, computer = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()


