#Realize 4 task with divide
#Реализовать задачу по угадыванию в минимальное количество попыток со стороны компьютера

# Description:
# Реализуем версию в которой используется человеческий подход
# Я загадал 6
# Компьютер назвал 50 - ровно половину от 100
# 50 больше 6
# 2 попытка это уменьшение в сторону 0 - 25
# 6 меньше, 3 попытка это 12
# -------   Если было загадано число 13? -----------
# 6 меньше, следующее число это 6, я угадал, в этом варианте угадал с 4 попытки
# Но если число 13? На 3 попытке при числе 12 оно меньше 13 => 25 - 12 = 13 (12) => 12 + 6 => 4 попытка это 18
# 18 больше чем 12 => 18 - 12 = 6 => 18 - 3 = 15, 5 попытка это 15
# 13 меньше 15 =>

# Псевдокод:
# numb = max(list_numb)//2
# Если число больше загаданного
#     --
# Если число меньше загаданного
#     numb = numb//2
#
# human_number = int(input('Write number from 1 to 100'))
# list_numb = [i for i in range(1,101)]

import random as r

guess_numb = r.randint(1,100)
list_numb = [i for i in range(1,102)]
numb = max(list_numb) // 2
count = 1

while True:
    if guess_numb == numb:
        print('Maybe {}? Yes! Victory!'.format(numb)); break
    elif guess_numb > numb:
        print('Maybe {}? No. Your numb more'.format(numb))
        list_numb = list_numb[list_numb.index(numb):]
    elif guess_numb < numb:
        print('Maybe {}? No. Your numb less'.format(numb))
        list_numb = list_numb[:list_numb.index(numb) + 1]
    numb = max(list_numb) - len(list_numb) // 2
    count += 1
print('\nNumber guessed - {}.\nAttempts are {}.'.format(guess_numb, count))