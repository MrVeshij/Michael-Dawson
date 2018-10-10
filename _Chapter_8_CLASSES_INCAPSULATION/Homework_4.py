# 4)Напишите программу «Зооферма», в которой будет создано несколько объектов класса Critter, а манипулиро­
# вать ими всеми можно будет с помощью списка. Теперь пользователь должен заботиться не об одной зверюш­
# ке, а обо всех обитателях зоофермы. Выбирая пункт в меню, пользователь выбирает действие, которое хотел
# бы выполнить со всеми зверюшками: покормИ1Ь их, поиграть с ними или узнать об их самочувствии. Чтобы
# программа была интереснее, при создании каждой зверюшки следует назначать ей случайно выбранные
# уровни голода и уныния.

# Псевдокод:
# Класс критер отвечает за 1 зверюшку
# Класс зооферма отвечает за n количество зверюшек
# Встроенные функции зверюшек измененены обеспечивая рандомный уровень голода и уныния при создании

import random as r


class Critter():
    """Virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        info = 'Name:' + self.name + '\n' + 'Boredom:' + str(self.boredom) + '\n' + 'Hunger:' + str(self.hunger) + '\n'
        return info

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'super'
        elif 5 <= unhappiness <= 10:
            m = 'normally'
        elif 11 <= unhappiness <= 15:
            m = 'not good'
        else:
            m = 'terrible'
        return m

    def talk(self):
        print('My name', self.name, ', and now i feel', self.mood, '\n')
        self.__pass_time()

    def eat(self, food = 4):
        print('Mrrr...Thanks!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print('Uiiii!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    print('You have farm. An your farm live 3 pets.')
    crit_name = input("How you rename number one?")
    crit_name2 = input('How you rename number two?')
    crit_name3 = input('HOw you rename number three?')
    crit = Critter(crit_name, hunger = r.randint(0,50), boredom = r.randint(0,50))
    crit2 = Critter(crit_name2, hunger = r.randint(0,50,), boredom = r.randint(0,50))
    crit3 = Critter(crit_name3, hunger = r.randint(0,50,), boredom = r.randint(0,50))
    choice = None
    while choice != "0":
        print(
            """
            My pet:
            0 - Exit
            1 - Learn about sensation your pets
            2 - Feed pets
            3 - Played with pets
            """)
        choice = input('You deal...')
        if choice == "0":
            print("Goodbye.")
        elif choice == "1":
            crit.talk()
            crit2.talk()
            crit3.talk()
        elif choice == "2":
            crit.eat()
            crit2.eat()
            crit3.eat()
        elif choice == "3":
            crit.play()
            crit2.play()
            crit3.play()
        elif choice == 'info':
            print(crit)
            print(crit2)
            print(crit3)
        else:
            print("Sorry. That choice miss")


main()
input("Press enter for exit")
