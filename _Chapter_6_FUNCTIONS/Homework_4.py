# 4)Напишите такую функцию computer_move(), которая сделала бы стратегию компьютера безупречной.
# Проверьте, можно ли создать непобедимого противника.


#По итогу это не помогает, а только ломает логику, дополнительно
#  по ходам в крсетиках ноликах смотрить ниже
# https://4brain.ru/blog/%D0%BA%D0%B0%D0%BA-%D0%B2%D1%8B%D0%B8%D0%B3%D1%80%D0%B0%D1%82%D1%8C-%D0%B2-%D0%BA%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D0%BD%D0%BE%D0%BB%D0%B8%D0%BA%D0%B8/


X = "X"
O = "O"
EMPTY = " "
TIE = 'TIE'
NUM_SQUARES = 9

WAYS_TO_WIN = ((0, 1, 2),
               (3, 4, 5),
               (6, 7, 8),
               (0, 3, 6),
               (1, 4, 7),
               (2, 5, 8),
               (2, 4, 6))

TRICKY_MOVES = ((0, 8),
               (2, 6))

PASS_MOVES = {(0, 4): 6,
              (2, 4): 8,
              (4, 6): 0,
              (4, 8): 2}

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
    print('computer', computer)
    print('human', human)
    print("I choose square", end=" ")
    for move in legal_moves(board): # Проверка на победителя, если пк на следующий ход побеждает этот ход в приоритете
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board): # Проверка на победителя - юзера, если на слудующий ход юзер побеждает - это ход №2
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in TRICKY_MOVES: # Если игрок применяет метод углового начала игры - приоритет №3     # Проверяет на угловые уловки
        if board[move[0]] == board[move[1]] == human != EMPTY :
            print('7')
            return 7
    for move in PASS_MOVES: # Если игрок тупит, пк ставит вилку - приоритет №4    # Проверка на упущенную вилку
        if board[move[0]] == board[move[1]] == computer != EMPTY:
            print(PASS_MOVES[move])
            return PASS_MOVES[move]
    for move in BEST_MOVES: # Если вышеуказанные проверки не дали результата - ходи выбирается из максимально оптимальных ходов
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