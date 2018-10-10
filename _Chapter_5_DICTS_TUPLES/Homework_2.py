# 2)Напишите программу «Генератор персонажей» для ролевой игры. Пользователю должно быть предоставлено
# 30  пунктов, которые можно распределить между четырьмя характеристиками: Сипа, Здоровье, Мудрость
# и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего «Пупа», но и воз­
# вращать их туда из характеристик, которым он решит присвоить другие значения.

# Псевдокод:
# 4 параметра - 4 переменные
# пул 30 баллов
# хер знает что тут писать, попробую реализовать вживую

wisdom = 0
strength = 0
agility = 0
health = 0
pull = 30

while True:
    print("""
    You have 4 characteristic:
    Wisdom = {}
    Strength = {}
    Health = {}
    Agility = {}
    
    At the moment you have {} points.
    
    -------------------------------------------------------------------------------------------------
    +W - increase Wisdom by 1 point ; -W - reduce by 1 point
    +S - increase Strength by 1 point ; -S - reduce by 1 point
    +H - increase Health by 1 point ; -H - reduce by 1 point
    +A - increase Agility by 1 point; -A - reduce by 1 point
    stop - enter for finish the calculation of characteristic
    \n\n\n""".format(wisdom,strength,agility,health,pull))

    request = input('Enter value: \n')
    if request == 'stop' : break
    elif request == '+W' and pull != 0 : wisdom += 1 ; pull -= 1
    elif request == '-W' and wisdom > 0 : wisdom -= 1 ; pull += 1
    elif request == '+S' and pull != 0 : strength += 1 ; pull -= 1
    elif request == '-S' and strength > 0 : strength -= 1 ; pull += 1
    elif request == '+H' and pull != 0 : health += 1 ; pull -= 1
    elif request == '-H' and health > 0: health -= 1 ; pull += 1
    elif request == '+A' and pull != 0 : agility += 1 ; pull -= 1
    elif request == '-A' and agility > 0 : agility -= 1 ; pull += 1



