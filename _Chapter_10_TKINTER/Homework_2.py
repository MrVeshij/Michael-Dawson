# 2) Перепишите игру «Отгадай число» из главы 3: создайте для нее графический интерфейс.



import random as r
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.riddle_number = r.randint(1, 100)
        self.count = 1


    def create_widgets(self):
        Label(self,
              text = 'Computer think number from 1 to 100, you have 10 attempts for guess him.'
              ).grid(row = 0, column = 0, sticky = W)

        Label(self,
              text = 'Input number'
              ).grid(row = 1, column = 0, sticky = W)
        self.inp_ent = Entry(self) # Check syntax
        self.inp_ent.grid(row = 2, column = 0, sticky = W)

        Button(self,
               text = 'Guess',
               command = self.logic_button
               ).grid(row = 3, column = 0, sticky = W)

        self.info_text = Text(self, width = 50, height = 10, wrap = WORD)
        self.info_text.grid(row = 4, column = 0)



    def logic_button(self):
        player_number = int(self.inp_ent.get())

        if player_number == self.riddle_number:
            self.info_text.delete(0.0, END)
            self.info_text.insert(0.0,'You win!Riddle number is {}. Attempt times is {}'.format(self.riddle_number, self.count) )
        elif player_number > self.riddle_number:
            self.info_text.delete(0.0, END)
            self.info_text.insert(0.0, 'Your number more.\nAttempt number {}'.format(self.count))
            self.count += 1
        elif player_number < self.riddle_number:
            self.info_text.delete(0.0, END)
            self.info_text.insert(0.0, 'Your number less.\nAttempt number {}'.format(self.count))
            self.count += 1
        if self.count > 10:
            self.info_text.delete(0.0, END)
            self.info_text.insert(0.0, 'Number of attempt more 10. You lose.')


def main():
    root = Tk()
    root.title('Guess number.')
    app = Application(root)
    app.mainloop()

main()