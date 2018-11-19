# 3) Напишите программу «Счет, пожалуйста!». Она должна показать пользователю несложное ресторанное меню
# с блюдами и ценами, принять его заказ и вывести на экран сумму счета.

# Псевдокод:
# Название проги - счет пожалуйста
# 1 лэб - Ресторанное меню
# 1 блок -  первые блюда( 1 лэб + 3 радиокнопки)
# 1 блок -  вторые блюда( 1 лэб + 3 радиокнопки)
# 1 блок -  особенные блюда( 1 лэб + 3 радиокнопки)
# Закуски - 5 вариантов
# Напитки - 5 вариантов
# Поле чаевые (логика расчета от общей суммы)
# Поле вывода содержит перечисление блюд + общую сумму

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        Label(self,
              text = 'Restaurant menu:'
              ).grid(row = 0, column = 1, sticky = W)

        Label(self,
              text = 'First dishes:'
              ).grid(row = 1, column = 0, sticky = W)
        self.first_dishes = StringVar()
        self.first_dishes.set(None)
        dishes1 = ['Borsch: 10$', 'Beetrout soup: 15$', 'Kharcho: 20$']
        row1 = 2
        for dish in dishes1:
            Radiobutton(self,
                        text = dish,
                        variable = self.first_dishes,
                        value = dish
                        ).grid(row = row1, column = 0, sticky = W)
            row1 += 1
        Label(self,
              text = 'Second dishes:'
              ).grid(row = 1, column = 1, sticky = W)
        self.second_dishes = StringVar()
        self.second_dishes.set(None)
        dishes2 = ['Potatoes with meat: 30$', 'Red fish with rice: 45$', 'Steak from marble beef: 60$']
        row2 = 2
        for dish in dishes2:
            Radiobutton(self,
                        text = dish,
                        variable = self.second_dishes,
                        value = dish
                        ).grid(row = row2, column = 1, sticky = W)
            row2 += 1

        Label(self,
              text = 'Specials dishes:'
              ).grid(row = 1, column = 2, sticky = W)
        self.special_dishes = StringVar()
        self.special_dishes.set(None)
        dishes3 = ['Pancakes with red roe: 100$', 'Ear elephant: 200$', 'Pike: 500$']
        row3 = 2
        for dish in dishes3:
            Radiobutton(self,
                        text = dish,
                        variable = self.special_dishes,
                        value = dish
                        ).grid(row = row3, column = 2, sticky = W)
            row3 += 1

        Label(self,
              text = 'Snacks:'
              ).grid(row = 5, column = 0, sticky = W)
        self.crisp = BooleanVar()
        Checkbutton(self,
                    text = 'Crisp: 3$',
                    variable = self.crisp
                    ).grid(row = 6, column = 0, sticky = W)
        self.cookie = BooleanVar()
        Checkbutton(self,
                    text = 'Cookie: 2$',
                    variable = self.cookie
                    ).grid(row = 6, column = 1, sticky = W)
        self.sausage = BooleanVar()
        Checkbutton(self,
                    text = 'Sausage: 5$',
                    variable = self.sausage
                    ).grid(row = 6, column = 2, sticky = W)

        Label(self,
              text = 'Drinks:'
              ).grid(row = 7, column = 0, sticky = W)
        self.tea = BooleanVar()
        Checkbutton(self,
                    text = 'Tea: $4',
                    variable = self.tea
                    ).grid(row = 8, column = 0, sticky = W)
        self.coffee = BooleanVar()
        Checkbutton(self,
                    text = 'Coffee: 8$',
                    variable = self.coffee
                    ).grid(row = 8, column = 1, sticky = W)
        self.juice = BooleanVar()
        Checkbutton(self,
                    text = 'Juice: 5$',
                    variable = self.juice
                    ).grid(row = 8, column = 2, sticky = W)

        Label(self,
              text = 'How much %tip from\n main price you will give?'
              ).grid(row = 10, column = 0, sticky = W)
        self.tip_ent = Entry(self)
        self.tip_ent.grid(row = 11, column = 0, sticky = W)

        self.info = Text(self, width = 65, height = 20, wrap = WORD)
        self.info.grid(row = 14, column = 0, columnspan = 10, sticky = W)

        Button(self,
               text = 'Calculate',
               command = self.do_info
                   ).grid(row = 12, column = 2, sticky = W)


    def do_info(self):
        first_dish = self.first_dishes.get()
        if first_dish != 'None':
            print(first_dish, type(first_dish))
            first_dish_price = int(str(first_dish.split(':')[-1:])[3:5])
        else:
            first_dish_price = 0
            first_dish = ''
        second_dish = self.second_dishes.get()
        if second_dish != 'None':
            second_dish_price = int(str(second_dish.split(':')[-1:])[3:5])
        else:
            second_dish_price = 0
            second_dish = ''
        special_dish = self.special_dishes.get()
        if special_dish != 'None':
            special_dish_price = int(str(special_dish.split(':')[-1:])[3:6])
        else:
            special_dish_price = 0
            special_dish = ''
        snacks = ''
        snacks_price = 0
        if self.crisp.get():
            snacks += 'Crisp: 3$\n'
            snacks_price += 3
        if self.cookie.get():
            snacks += 'Cookie: 2$\n'
            snacks_price += 2
        if self.sausage.get():
            snacks += 'Sausage: 5$\n'
            snacks_price += 5
        drinks = ''
        drinks_price = 0
        if self.tea.get():
            drinks += 'Tea: 4$\n'
            drinks_price += 4
        if self.coffee.get():
            drinks += 'Coffee: 8$\n'
            drinks_price += 8
        if self.juice.get():
            drinks += 'Juice: 5$\n'
            drinks_price += 5
        tip = self.tip_ent.get()
        if tip:
            tip = int(tip)
            if tip not in range(1,101):
                tip = None
        expense = 'Your order.\n\nMain dishes:\n'
        expense += first_dish + '\n' + second_dish + '\n' + special_dish
        expense += '\n\nSnacks:\n' + snacks
        expense += '\n\nDrinks:\n' + drinks

        order_sum = (first_dish_price +
                     second_dish_price +
                     special_dish_price +
                     snacks_price +
                     drinks_price)
        if tip:
            order_sum = ((order_sum/100) * tip) + order_sum

        expense += '\n\n' + str(order_sum) + '$'

        self.info.delete(0.0, END)
        self.info.insert(0.0, expense)





def main():
    root = Tk()
    root.title('Expense, please')
    app = Application(root)
    app.mainloop()


main()