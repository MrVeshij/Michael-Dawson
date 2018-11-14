# 2)Доработайте игру «Опадай число» из главы З так, чтобы в ней нашла применение функция ask_number().

import random as r

riddle_number = r.randint(1,100)
count = 1
question = "Input number from 1 to 100\n"

def  ask_number(question, low, high, step = 1):
    """Просит  ввести  число  из  диапазона."""
    response = None
    while  response  not  in  range(low, high, step):
        response = int(input(question))
    return  response




while True:
    player_number = ask_number(question, 1, 101)
    if player_number == riddle_number:
        print('You win!Riddle number is {}. Attempt times is {}'.format(riddle_number, count))
        break
    elif player_number > riddle_number:
        print('Your number more')
    elif player_number < riddle_number:
        print('Your number less')

    count += 1
    if count >= 10:
        print('You lose. Number of attempt more 10.')
        break