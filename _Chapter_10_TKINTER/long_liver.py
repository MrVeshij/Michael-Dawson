from tkinter import *


class Application(Frame):
    """GUI - application, have secret long years"""
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Create button, text field and text scope"""
        self.inst_lbl = Label(self, text = 'To learn secret long years, input password.')
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.pw_lbl = Label(self, text = 'Password: ')
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        self.submit_bttn = Button(self, text = 'Learn secret', command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)


    def reveal(self):
        """One password - one answer, another password - another answer"""
        contents = self.pw_ent.get()
        if contents == 'secret':
            message = 'For long life to 100 years, first live to 99,'\
                      'and after be VERY careful.'
        else:
            message = 'You input wrong password, i can\'t share ' \
                      'that secret with you'

        self.secret_txt.delete(0.0,END)
        self.secret_txt.insert(0.0, message)



root = Tk()
root.title('Long-living')
root.geometry('400x150')
app = Application(root)
root.mainloop()

