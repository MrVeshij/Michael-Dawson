# 1)Создайте программу, которая будет выводить список слов в случайном порядке. На экране должны печататься
# без повторений все слова из представленного списка.

# Псевдокод:
# Модуль рандом
# метод shuffle
# вывод списка слов

#Если пользователь хочет ввести слова для списка, можно воспользоваться циклом со словом "stop" или принимать на
#на вход слова и делить их через цикл for

import random as r

#list_word = list(input('Input some words'))
inner_list_word = ['sun','sky','horse']
r.shuffle(inner_list_word)

print(inner_list_word)

