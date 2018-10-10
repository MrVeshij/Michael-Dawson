# 3)Создайте в программе «Моя зверюшка» своего рода «черный ход» - способ увиде1Ь точные значения чи­
# словых атрибутов объекта. Сделайте в меню секретный пункт, который подсказка не будет отражать, и, если
# пользователь его выберет, выводите объект на экран (для этого в классе Critter должен бы1Ь реализован
# специальный метод _str_()).

class Critter():
    """Virtual pet"""
    def __init__(self, name, hunger =0, boredom= 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        info = 'Boredom:' + str(self.boredom) + '\n' + 'Hunger:' + str(self.hunger)
        return info

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'super'
        elif 5 <= unhappiness <= 10:
            m = 'normally'
        elif 11 <= unhappiness <= 15:
            m = 'not good'
        else:
            m = 'terrible'
        return m

    def talk(self):
        print('My name', self.name, ', and now i feel', self.mood, '\n')
        self.__pass_time()

    def eat(self, food = 4):
        print('Mrrr...Thanks!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print('Uiiii!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("How you rename your pet?")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print(
            """
            My pet:
            0 - Exit
            1 - Learn about sensation pet
            2 - Feed pet
            3 - Played with pet
            """)
        choice = input('You deal...')
        if choice == "0":
            print("Goodbye.")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        elif choice == 'info':
            print(crit)
        else:
            print("Sorry. That choice miss")

main()
input("Press enter for exit")
