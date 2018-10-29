# Description:
# Перенести логику в графический интерфейс
# Пользователь видит на экране количество свободных очков и куда они были вложены
# С помощью 8 кнопок он может распределять общий пул очков между 4 характеристиками

# Pseudocode:
# Создаем 8 кнопок с отсылкой на логику прибавки
# Поле текст выводим на верх по центру.
# ммм реализация с 8 функциями, как то топорно - должен быть более элегантный способ
# Думаю это можно реализовать 2 функциями которые принимают на вход признак "уменьшения" или "увеличиения"

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.wisdom = 0
        self.strength = 0
        self.agility = 0
        self.health = 0
        self.pull = 30
        self.create_widgets()

    def create_widgets(self):
        self.info = Text(self, width = 40, height = 8, wrap = WORD)
        self.info.grid(row = 0, column = 0, columnspan = 2,rowspan = 3, sticky = W)
        self.do_text()

        Button(self,
               text = 'Increase WISDOM',
               command = self.w_inc
               ).grid(row = 6, column = 0, sticky = W)

        Button(self,
               text = 'Reduce WISDOM',
               command = self.w_red
               ).grid(row = 6, column = 1, sticky = W)

        Button(self,
               text = 'Increase STRENGTH',
               command = self.s_inc
               ).grid(row = 7, column = 0, sticky = W)

        Button(self,
               text = 'Reduce STRENGTH',
               command = self.s_red
               ).grid(row = 7, column = 1, sticky = W)

        Button(self,
               text = 'Increase HEALTH',
               command = self.h_inc
               ).grid(row = 5, column = 0, sticky = W)

        Button(self,
               text = 'Reduce HEALTH',
               command = self.h_red
               ).grid(row = 5, column = 1, sticky = W)

        Button(self,
               text = 'Increase AGILITY',
               command = self.a_inc
               ).grid(row = 4, column = 0, sticky = W)

        Button(self,
               text = 'Reduce AGILITY',
               command = self.a_red
               ).grid(row = 4, column = 1, sticky = W)


    def w_inc(self):
        if self.pull != 0:
            self.wisdom += 1
            self.pull -= 1
            self.do_text()


    def w_red(self):
        if self.wisdom > 0:
            self.wisdom -= 1
            self.pull += 1
            self.do_text()


    def s_inc(self):
        if self.pull != 0:
            self.strength += 1
            self.pull -= 1
            self.do_text()


    def s_red(self):
        if self.strength > 0:
            self.strength -= 1
            self.pull += 1
            self.do_text()


    def h_inc(self):
        if self.pull != 0:
            self.health += 1
            self.pull -= 1
            self.do_text()


    def h_red(self):
        if self.health > 0:
            self.health -= 1
            self.pull += 1
            self.do_text()


    def a_inc(self):
        if self.pull != 0:
            self.agility += 1
            self.pull -= 1
            self.do_text()


    def a_red(self):
        if self.agility > 0:
            self.agility -= 1
            self.pull += 1
            self.do_text()


    def do_text(self):
        text = ("""
    You have 4 parameters:
    Wisdom = {}
    Strength = {}
    Health = {}
    Agility = {}

    At the moment you have {} points.
    """.format(self.wisdom, self.strength,  self.health, self.agility, self.pull))
        self.info.delete(0.0, END)
        self.info.insert(0.0, text)



def main():
    root = Tk()
    root.title('Graphic version module distribution characteristic')
    app = Application(root)
    app.mainloop()

main()



