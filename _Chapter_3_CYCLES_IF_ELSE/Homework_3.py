# 3)О Измените программу «Отгадай число» таким образом, чтобы у игрока было ограниченное количество попы­
# ток. Если игрок не укладывается в заданное чисnо (и проигрывает), то программа должна выводить сколь
# возможно суровый текст.


# Псевдокод:
# Компьютер загадывает число от 1 до 100
# Человеку предлагается ввести число, если оно совпадает с загаданным
# победа. Иначе следующая попытка.
# Все выполняется в цикле, дается 10 попыток при 10 попытке поражение игрока

import random as r

riddle_number = r.randint(1,100)
count = 1

while True:
    player_number = int(input("Input number from 1 to 100\n"))
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
