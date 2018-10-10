# 4)О А вот задача посложнее. Напишите на псевдокоде алгоритм игры, в которой случайное число от 1 до 100 за­
# гадывает человек, а отгадывает компьютер. Прежде чем приступать к решению, задумайтесь над тем, какой
# должна быть оптимальная стратегия опадывания. Если алгоритм на псевдокоде будет удачным, попробуйте
# реализовать игру на Pythoп.

# Псевдокод:
# Человек загадывает число от 1 до 100 через инпут.
# Компьютер в цикле начинает угадывать число
# Самый простой вариант перебор от 1 до 100. Но он самый долгий.
# Быстрый - логика из ифов для деления на 2 - попробовал, но это все тянет на строк 50, как то криво получается
# Реализовал вариант с рандомным вариантом

import random as r

human_number = int(input('Input number from 1 to 100'))
count = 1
victory = 'Machine win! Riddle number is {}.'.format(human_number, count)
attempt_more = 'I try, but my number is more'
attempt_less = 'I try, but my number is less'


while True:
    computer_number = r.randint(1,100)
    print('Attempt {}'.format(count))
    if computer_number == human_number:
        print(victory, 'Times attempts is {}'.format(count))
        break
    count += 1
