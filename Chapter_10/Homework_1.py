#  1) Напишите собственную версию «Сумасшедшего сказочника>>, в которой система элементов управления внутри
# окна будет другой.

# Description:
# Какие объекты будем использовать
# Части тела - выбор из 5 частей
# Прилагательные - 2 состояния на выбор
# Человек имя
# Сущеста мн
# Глагол
#
# Рассположение
# Текст выводится справа (пол окошка)
# первый блок - левый верхний угол это части тела выбор из 5 столбик(реализовать через список)
# второй блок слева вверху в столбик 2 прилагательные
# лэйблы пускаем вниз от прилагательных



from tkinter import *


class Application(Frame):
    """GUI application, create story on base input user"""
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        Label(self,
              text = 'Fill information for create story.'
              ).grid(row = 0, column = 3, sticky = W)

        Label(self,
              text = 'Choose one body part.'
              ).grid(row = 1, column = 0, sticky = W)
        self.body_part = StringVar()
        self.body_part.set(None)
        body_parts = ['nose', 'month', 'cheek', 'ear', 'eye']
        row = 2
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = row, column = 0, sticky = W)
            row += 1

        Label(self,
              text = 'Choose condition'
              ).grid(row = 7, column = 0, sticky = W)

        self.cond1 = BooleanVar()
        Checkbutton(self,
                    text = 'Aggressive ',
                    variable = self.cond1
                    ).grid(row = 7, column = 1, sticky = W)

        self.cond2 = BooleanVar()
        Checkbutton(self,
                    text = 'Friendly',
                    variable = self.cond2
                    ).grid(row = 7, column = 2, sticky = W)

        Label(self,
              text = 'Human name'
              ).grid(row = 2, column = 1, sticky = W)
        self.h_name = Entry(self)
        self.h_name.grid(row = 2, column = 2, sticky = W)

        Label(self,
              text = 'Noun in plural'
              ).grid(row = 3, column = 1, sticky = W)
        self.noun = Entry(self)
        self.noun.grid(row = 3, column = 2, sticky = W)

        Label(self,
              text = 'Verb in infinitive '
              ).grid(row = 4, column = 1, sticky = W)
        self.verb = Entry(self)
        self.verb.grid(row = 4, column = 2, sticky = W)

        self.story_txt = Text(self, width = 50, height = 20, wrap = WORD)
        self.story_txt.grid(row = 1, column = 3, rowspan = 7)

        Button(self,
               text = 'Get story',
               command = self.tell_story
               ).grid(row = 6, column = 1, sticky = W)



    def tell_story(self):
        """Fills text scope next story an base user input"""
        person = self.h_name.get()
        noun = self.noun.get()
        verb = self.verb.get()
        adjectives = ''
        if self.cond1.get():
            adjectives += 'aggressive '
        if self.cond2.get():
            adjectives += 'friendly '
        body_part = self.body_part.get() # Через метод get получаем доступ к value
        # create story
        story = 'Famous traveller '
        story += person
        story += ' despaired finished case yourself life - search'\
        ' lost city, in whom, on legend, dwell '
        story += noun.title() # ERROR - DELETE
        story += '. But once '
        story += noun
        story += ' and '
        story += person + ' meet face to face. '
        story += 'Powerful '
        story += adjectives
        story += ' sense captured soul traveller. '
        story += 'After many years searches, aim was achieved. '
        story += person
        story += ' sense, how on his ' + body_part + ' roll down tear. '
        story += 'And suddenly '
        story += noun
        story += ' go to attack, and '
        story += person + ' was momentarily was devoured.'
        story += '\nMoral? If though '
        story += verb
        story += ', do that with carefully.'
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

root = Tk()
root.title('Crazy storyteller')
app = Application(root)
app.mainloop()



