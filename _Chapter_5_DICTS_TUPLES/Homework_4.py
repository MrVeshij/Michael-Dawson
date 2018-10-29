# 4)Доработайте программу «Кто твой папа?» так, чтобы можно было, введя имя человека, узнать, кто его дед.
# Программа должна по-прежнему пользоваться одним словарем с парами «сын - отец». Подумайте, как
# включить в этот словарь несколько поколений.



dict_pairs = {'vova':['Jenia','Kostia'],
              'oksana':['Vova', 'Oleg'],
              'jenia':['Kostia', 'Petr'],
              'masha':['Kostia', 'Petr']}

while True:
    print("""
    Learn who is your daddy and grandfather.
    Enter name and you learn.
    ------------------------------------------------------------------
    stop - finish
    add - add or change pair
    del - delete existing pair
    """)
    request = input('Waiting for input: \n').lower()
    print(request)
    if request == 'stop' : break
    elif request in dict_pairs : print('His father is {}, and grandfather {}'.format(dict_pairs[request][0],dict_pairs[request][1]))
    elif request == 'add' : dict_pairs[input('Enter name child\n')] = input('Enter name father\n'), input('Enter name grandfather\n')
    elif request == 'del' : del dict_pairs[input('Enter name child for delete pair\n')]
    else : print('That name not determined.\n')