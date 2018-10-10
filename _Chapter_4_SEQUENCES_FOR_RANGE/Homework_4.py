# 4)Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его опадать. Компьютер
# сообщает игроку, сколько букв в слове, и дает пяtь попыток узнаtь, есtь ли какая-либо буква в слове, причем
# программа может отвечаtь только «Да» и «Her». Вслед за тем игрок должен попробовать отгадать слово.

# Псевдокод:
# Список слов, рандом и вывод человеческий через цифру 3
# Функция лен
# Счетчик на 5 попыток
# При вводе буквы компьютер проверяет вхождение
# После пятой попытки дается возможность угадать слово
# Если не угадываешь - то ты лох)

import random as r

list_words = ['orange', 'rainbow', 'boobs']
random_numb = r.randint(0,2)
random_word = list_words[random_numb]
count = 0
length_word = len(random_word)
attempts = 5

while True:
    print('Guess word have {} letters. You have {} attempts for guess letters'.format(length_word, attempts))
    attempt_letter = input('Input letter for hint\n')
    if attempt_letter in random_word:
        print('Yes')
    else:
        print('No')
    count += 1
    attempts -= 1
    if count == 5:
        attempt_word = input('Time gone. Input word entirely.\n')
        if attempt_word == random_word:
            print('Wow. You win.')
            break
        else:
            print('Looser.')
            break