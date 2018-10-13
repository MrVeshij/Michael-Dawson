from tkinter import *


class Application(Frame):
    """GUI application, create story on base input user"""
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Create elements control, with help themselves user
        will input initial data and get finished story"""
        Label(self,
              text = 'Input data for create new stry'
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        Label(self,
              text = 'Name human: '
              ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)

        Label(self,
              text = 'Noun in plural: '
              ).grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)

        Label(self,
              text = 'Verb in infinitive: '
              ).grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)

        Label(self,
              text = 'Adjective (s): '
              ).grid(row = 4, column = 0, sticky = W)

        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = 'impatient',
                    variable = self.is_itchy
                    ).grid(row = 4, column = 1, sticky = W)

        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text = 'joyful',
                    variable = self.is_joyous
                    ).grid(row = 4, column = 2, sticky = W)

        self.is_penetrating = BooleanVar()
        Checkbutton(self,
                    text = 'penetrating',
                    variable = self.is_penetrating
                    ).grid(row = 4, column = 3, sticky = W)

        Label(self,
              text = 'Body Part:'
              ).grid(row = 5, column = 0, sticky = W)
        self.body_part = StringVar()
        self.body_part.set(None)
        body_parts = ['navel', 'big toe', 'medulla']
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1

        Button(self,
               text = 'Get story',
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)
        self.story_txt = Text(self, width = 75, height =  10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)


    def tell_story(self):
        """Fills text scope next story an base user input"""
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ''
        if self.is_itchy.get():
            adjectives += 'impatient'
        if self.is_joyous.get():
            adjectives += 'joyful'
        if self.is_penetrating.get():
            adjectives += 'penetrating'
        body_part = self.body_part.get()
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



