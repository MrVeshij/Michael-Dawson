# 2)О Напишите программу, которая бы «Подбрасывала» условную монету 100 раз и сообщала, сколько раз выпал
# орел, а сколько  - решка.

# Псевдокод:
# Цикл с использованием словаря где орел 1 а решка 2
# Встроенные счетчики для подсчета количества орлов и решек

import random as r


#dict_choose = {1:'Head', 2:'Tails'}
main_count = 0
head = 0
tails = 0

while main_count != 100:
    main_count += 1
    random_choose = r.randint(1, 2)
    if random_choose == 1:
        head += 1
    else:
        tails += 1

print('You flip coin 100 times. Heads is {}, Tails is {}'.format(head,tails))
