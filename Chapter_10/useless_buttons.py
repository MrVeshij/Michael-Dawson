from tkinter import *

root = Tk()
root.title('Useless buttons')
root.geometry('200x85')
app = Frame(root)
app.grid()
bttn1 = Button(app, text = 'I\'am do nothing')
bttn1.grid()
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = 'And I too')
bttn3 = Button(app)
bttn3.grid()
bttn3['text'] = 'And i'
root.mainloop()
