# 1)Напишите программу- симулятор пирожка с «сюрпризом», - которая бы при запуске отображала один из
# пяти различных «Сюрпризов», выбранный случайным образом.

#Псевдокод:
#Рандомное число от 1 до 5 выдает результат пирожка с сюрпризом

import random

random_choose = random.randint(1,5)
dict_pie = {1:'pie with fish',
            2:'pie with cherry',
            3:'pie with carrot',
            4:'pie with onion',
            5:'pie with meat'
            }

print('You take pie. It\'s {}'.format(dict_pie[random_choose]))