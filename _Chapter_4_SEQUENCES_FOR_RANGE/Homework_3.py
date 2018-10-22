#  3)Доработайте игру «Анаграммы» так, чтобы к каждому слову полаrалась подсказка. Игрок должен получать
# право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления
# очков, по которой бы иrроки, опадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Псевдокод:
# Есть список слов в словаре с подсказкой
# Игроку выводится слово в измененном в виде с помощью модуля рандом
# Игрок в цикле вводит свою верскию слова
# Если игрок угадывает слово без подсказки получает 10 баллов
# Иначе 5

import random as r

dict_words = {
    'orange':'Cool fruit',
    'rainbow':'behold after rain',
    'boobs':'mmmm, sexy'
}

list_words = ['orange','rainbow','boobs']
random_word = r.choices(list_words)
check_word = str(random_word[0])
random_word = list(random_word[0])
r.shuffle(random_word)
shuffle_word = ''
for i in random_word: shuffle_word += i

count = 0
points = 0
word_player = None

while True:
    word_player = input('Word change with anagram. Guess his:\n==={}===\n'.format(shuffle_word))
    if word_player == check_word:
        if count == 0:
            points = 10
            break
        else:
            points = 5
            break
    else:
        print('Nope, try again.')
        count += 1

    if count >= 5:
        print('Get hint looser!')
        print(dict_words[check_word])

print('You guess word! Congratulations! Your points is {}'.format(points))


