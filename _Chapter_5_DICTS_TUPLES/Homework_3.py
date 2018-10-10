# 3)Напишите программу «Кто твой папа?», в которой пользователь будет вводить имя человека, а програм­
# ма - называть отца этого человека. Чтобы было интереснее, можно «научить» программу родственным
# отношениям среди литературных персонажей, исторических лиц и современных знаменитостей. Предоставьте
# пользователю возможность добавлять, заменять и удалять пары «СЫН - отец».

# Псевдокод:
# Словарь со сынами-отцами
# В цикле дерево выбора из 3 вариантов
# Редакт существующего словаря

dict_pairs = {'Vova':'Jenia',
              'Oksana':'Vova',
              'Jenia':'Kostia',
              'Masha':'Kostia'}

while True:
    print("""
    Learn who is your daddy
    Enter name and you learn.
    ------------------------------------------------------------------
    stop - finish
    add - add new pair
    del - delete existing pair
    """)
    request = input('Waiting for input: \n')
    if request == 'stop' : break
    elif request in dict_pairs : print('His father is ', dict_pairs[request])
    elif request == 'add' : dict_pairs[input('Enter name child\n')] = input('Enter name father\n')
    elif request == 'del' : del dict_pairs[input('Enter name child for delete pair\n')]
    else : print('That name not define.\n')