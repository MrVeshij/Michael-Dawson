from tkinter import *


class Application(Frame):
    """GUI application, allowing choose loved genre movie"""
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Create elements, by which user will choose"""
        Label(self,
              text = 'Choose you favorite genre movie.'
              ).grid(row = 0, column = 0, sticky = W)

        Label(self,
              text = 'Choose everything, would you like:'
              ).grid(row = 1, column = 0, sticky = W)

        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                    text = 'Comedy',
                    variable = self.likes_comedy,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text = 'Drama',
                    variable = self.likes_drama,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        self.likes_romance = BooleanVar()
        Checkbutton(self,
                    text = 'Film about love',
                    variable = self.likes_romance,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)

        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)


    def update_text(self):
        """Update text element after user choose himself loved genres"""
        # В данном методе переменная likes каждый раз перезаписывается что приводит к тому
        # что строки располагаются в той последовательности что задаются внутри функции
        likes = ''
        if self.likes_comedy.get():
            likes += 'You like comedy.\n'
        if self.likes_drama.get():
            likes += 'You like drama.\n'
        if self.likes_romance.get():
            likes += 'You like films about love.\n'
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0,likes)
        print(likes)

root = Tk()
root.title('Film man')
app = Application(root)
app.mainloop()





