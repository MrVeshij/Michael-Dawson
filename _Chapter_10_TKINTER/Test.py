#Проверяем как работает класс tkinter StringVar()
# Когда функцией set принимается значение None - оно проходит какие то внутренние проверки, и
# выходе становится строковым значением "None", поэтому при проверка на значение variable класса Radiobutton,
# Это нужно учитывать, и понимать что там совсем не None , а что то хранится.

from tkinter import *

root = Tk()
app = Frame(root)


test = StringVar()
test.set(None)

Radiobutton(text = 'test',
            variable = test,
            value = 'testgfhf').grid(row = 0, column = 0)
print(test, type(test))
app.mainloop()
print(test, type(test))

