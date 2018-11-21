# 4)Создайте несложную объектно-ориентированную приключенческую игру, в которой игрок сможет менять свое
# местонахождение, перемещаясь каждый раз в одно из мест, ближайших к данному.

# В данной версии я реализовал возможность передвижения игрока к одному из 5 мест
# В новой версии надо реализовать ограничения по сетке, можно перемещаться только в одно из ближайших мест, не
# в дальнии

# Description:
# Есть игрок
# Мест 9 игрок находится в центре на девятом месте
# Логика передвижения, когда игрок может двигаться только к ближайшим от себя местностям по сетке
# - - -
# - * -
# - - -
# Для начала реализовать движения по местностям без логики
# Как реализовать систему передвижения, игрок должен ввести название местности чтобы в нее попасть, или номер местности
# Как он узнает это? На экран должен выводиться все местности
#
# Псевдокод:
# Класс игрок
# - включает в себя метод движение в котором перходит на новую местность
#
# Класс местность
# - имеет атрибут имя местности и атрибут номер в сетке


from games import ask_number


class Player():
    def __init__(self):
        self.name = 'Hero'
        self.current_landscape = None


    def __str__(self):
        return self.name + 'and now, i dwell in' + self.current_landscape


    def move(self, landscape):
        """Move hero to landscape"""
        print('\nHero move to', landscape)
        self.current_landscape = landscape

    def print_map(self,map):
        """Print current map with all changes"""
        count = 0
        for i in map:
            count += 1
            if count < 3:
                print('[ ', i, ' ]', end="")
            else:
                count = 0
                print('[ ', i, ' ]', end="")


class Landscape():
    def __init__(self,name, numb_matrix):
        self.name = name
        self.numb_matrix = numb_matrix


    def __str__(self):
        return self.name + '\t' + str(self.numb_matrix)





class Game():
    def __init__(self):
        self.player = Player()
        self.valley = Landscape('Valley', 1)
        self.town = Landscape('Town', 2)
        self.city = Landscape('City', 3)
        self.cave = Landscape('Cave', 4)
        self.field = Landscape('Field', 5)
        self.field = Landscape('Mount', 6)
        self.field = Landscape('Alone house', 7)
        self.field = Landscape('Forest', 8)
        self.field = Landscape('Inn', 9)
        self.places = [self.valley, self.town, self.city, self.cave, self.field]


    def play(self):
        self.player.move(self.city)
        while True:
            print('\nAvailable places: \n')
            for place in self.places:
                print(place)
            choice = ask_number('\nWill move?\n0 - for stop walking.', 0, 6)
            if choice == 0: break
            for place in self.places:
                if choice == place.numb_matrix:
                    self.player.move(place)



def main():
    game = Game()
    game.play()

main()

