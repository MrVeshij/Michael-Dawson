# 1)Доработайте программу «Моя зверюшка» так, чтобы пользователь мог сам решить, сколько еды скормить
# зверюшке и сколько времени потратить на игру с ней (в зависимости от передаваемых величин зверюшка
# должна неодинаково быстро насыщаться и веселеть).

class Critter():
    """Virtual pet"""
    def __init__(self, name, hunger =0, boredom= 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self,food = 0, fun = 0):
        if 5 <= food <= 9:
            self.hunger +=  2
            self.boredom += 2
        elif food > 9:
            self.hunger += 3
            self.hunger += 3
        elif 5 <= fun <= 9:
            self.hunger += 2
            self.boredom += 2
        elif fun > 9:
            self.hunger += 3
            self.boredom += 3
        else:
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
        food = int(input('How mach food you get pet?\n'))
        print('Mrrr...Thanks!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        fun = int(input('How mach fun you get pet?\n'))
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
        else:
            print("Sorry. That choice miss")

main()
input("Press enter for exit")
