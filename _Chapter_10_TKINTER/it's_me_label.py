from tkinter import *


root = Tk()
root.title('It\'s me, label.')
root.geometry('200x50')
app = Frame(root)
app.grid()
lbl = Label(app, text = 'It\'s me!')
lbl.grid()
root.mainloop()
