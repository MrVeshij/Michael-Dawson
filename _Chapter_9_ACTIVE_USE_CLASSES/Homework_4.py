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


AVAILABLE_PLACES = {1:(2,4,5),
                    2:(1,3,4,5,6),
                    3:(2,5,6),
                    4:(1,2,5,7,8),
                    5:(1,2,3,4,6,7,8,9),
                    6:(2,3,5,8,9),
                    7:(4,5,8),
                    8:(4,5,6,7,9),
                    9:(5,6,8)}

class Player:
    def __init__(self):
        self.name = 'Hero'
        self.current_landscape = None


    def __str__(self):
        return self.name + 'and now, i dwell in' + self.current_landscape


    def move(self, landscape):
        """Move hero to landscape"""
        print('\nHero move to', landscape, '\n')
        self.current_landscape = landscape

    def look_map(self,map):
        """Print current map with all changes"""
        count = 0
        for i in map:
            count += 1
            if count < 3:
                if isinstance(i,str):
                    print('[   ', i, '    ]', end="")
                else:
                    print('[ ', i.name, ' ]', end="")
            else:
                count = 0
                if isinstance(i, str):
                    print('[   ', i, '    ]')
                else:
                    print('[ ', i.name, ' ]')



class Landscape:
    """Fabric created a landscape"""
    def __init__(self,name,name_check, numb_matrix):
        self.name = name
        self.name_check = name_check
        self.numb_matrix = numb_matrix


    def __str__(self):
        return self.name



class Game:
    def __init__(self):
        self.player = Player()
        self.valley = Landscape('Valley','valley',1)
        self.field = Landscape('Field ','field',2)
        self.inn = Landscape('Inn   ','inn',3)
        self.cave = Landscape('Cave  ','cave',4)
        self.town = Landscape('Town  ','town',5)
        self.mount = Landscape('Mount ','mount',6)
        self.house = Landscape('House ','house',7)
        self.forest = Landscape('Forest','forest',8)
        self.city = Landscape('City  ','city',9)
        self.places = [self.valley, self.field, self.inn, self.cave, self.town,
                       self.mount, self.house, self.forest, self.city]


    def map(self,player):
        """Change list of places add hero in list"""
        map = self.places[:]
        map[player.current_landscape.numb_matrix - 1] = 'X'
        return map


    def play(self):
        self.player.current_landscape = self.town
        print('You begin your journey in small town country Rosaria.\n')
        while True:
            print("\nYou can:\ntire - Retirement\nmap - Look to the map\nroute - Choice route\n")
            choice = input('Your choice?\n').lower()
            if choice == 'tire':
                print('You\'re too tire...')
                break
            elif choice == 'map':
                print('\nYou look on your map.')
                self.player.look_map(self.map(self.player))
            elif choice == 'route':
                choice = input('Where you keep going?\nBack - on previous page\n').lower()
                while isinstance(choice,str):
                    if choice == 'back': break
                    for i in self.places:
                        if i.name_check == choice:
                            choice = i.numb_matrix
                            if choice in AVAILABLE_PLACES[self.player.current_landscape.numb_matrix]:
                                self.player.move(i)
                                break
                    else:
                        choice = input('You don\'t go there.Choice another path:\n').lower()



def main():
    game = Game()
    game.play()


main()

