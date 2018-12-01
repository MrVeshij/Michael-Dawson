# 2)Напишите игру, в которой на персонаж, управляемый игроком с помощью мыши, сверху (с «неба») будут
# падать какие-нибудь тяжелые объекты, а он должен будет уворачиваться.

# Description:
# Игра стрится на аналогии с игрой паника в пицерии:
# За исключением объекта повара все остальные классы сохраняются
# Предметы - булыжники
# Персонаж - ГГ готики
# Место действия храм разрушившийся после изгнания спящего
# При избегании булыжников игрок получает +1 уризель
# При попадании булыжником игрок получает сообщение, через осталось 2 недели, игра заканчивается
# После вывода сообщения булыжники исчезают

# Pseudocode:
# class rock - фабрика по созданию булыжников, появляются  в рандомной точке за экраном и падают вниз
# с постоянной скоростью
# class gg - Безымянный управляемый мышкой персоонаж, при попадании булыжником вызывается окно поражения
# main - основная функция инициирующая запуск игры

# 1. Сделать булыжники с нормальным отображением
# С трудом, сделал порядка 15 камней, и так и не понял как бороться с фоном, по итогу сделал булыжник типа кирпича
# Карина помогла скинула рабочией сайтец с добавлением прозрачного фона, наверн проблема была именно в нем.

# 2. Булыжник и ударвишийся герой должны замереть, остальные булыжники продолжают падать
# Вопрос как реализовать отключение персонажа от мышки
# Решил вопрос передачей значения (x) булыжника (x) гг

# 3. Доделать счет чтобы отбражались оставшиеся булыжники( 1000 - после их счета ГГ побеждает)
# 4. Ввести систему сложностей по аналогии с предыдущей игрой ( 4 уровня сложности )
# Реализовал оба пункта, сложность заключается в возрастании скорости, не стал
# делать несколько точек респа камней ибо для этого нужно будет продумывать новую логику с новыми классам
# Иначе не увидел возможности реализовать новые храмы, или можно функцию подсчета перенести в другой класс, тогда
# Можно реализовать, точно! Я придумал решение через перебор списка.


from livewires import games, color
import random as r

games.init()

class GG(games.Sprite):
    """Create GG from game gothic doge from rocks"""
    gg_image = games.load_image('gg.png')
    def __init__(self):
        super().__init__(GG.gg_image,
                         x = games.mouse.x,
                         bottom = games.screen.height,
                         )
        self.score = games.Text(value = 1000, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)
        self.check = 0
        self.copy = 0
        self.time_born = 0


    def update(self):
        self.x = games.mouse.x
        if self.left < 0: self.left = 0
        if self.right > games.screen.width: self.right = games.screen.width
        self.check_catch()
        self.difficult()
        if self.check:
            self.x = self.copy


    def check_catch(self):
        for rock in self.overlapping_sprites:
            self.end_game()
            if not self.check:
                self.copy = rock.x
                rock.dy = 0
                self.check = 1
            # Как заставить застыть упвший на голову булыжник
            # Решил вопрос перекопированием, теперь я понимаю что такое глубина в программирование)
            # И то что я херовый пловец


    def end_game(self):
        """End game"""
        ending_message = games.Message(value = "You get rock in head.Time to sleep.",
                                    size = 40,
                                    color = color.white,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 2 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(ending_message)


    def difficult(self):
        """Correct difficult in game"""
        # level 1, increase speed falling rocks
        if self.score.value == 750:
            lvl_1_msg = games.Message(value = 'Rocks fall faster!',
                          size = 90,
                          color = color.black,
                          x = games.screen.width/2,
                          y = games.screen.height/2,
                          lifetime = 0.5 * games.screen.fps)
            games.screen.add(lvl_1_msg)
            Rock.speed = 6
        # level 2, increase speed falling rocks
        if self.score.value == 500:
            lvl_1_msg = games.Message(value = 'Rocks fall still faster!!',
                          size = 90,
                          color = color.black,
                          x = games.screen.width/2,
                          y = games.screen.height/2,
                          lifetime = 0.5 * games.screen.fps)
            games.screen.add(lvl_1_msg)
            Rock.speed = 9
        # level 3, increase speed falling rocks
        if self.score.value == 250:
            lvl_1_msg = games.Message(value = 'Carefully!!!',
                          size = 90,
                          color = color.black,
                          x = games.screen.width/2,
                          y = games.screen.height/2,
                          lifetime = 0.5 * games.screen.fps)
            games.screen.add(lvl_1_msg)
            Rock.speed = 12
        # 0 points = victory
        if self.score.value == 0:
            victory_message = games.Message(value = 'You elude from all rocks! You save himself !',
                                            size = 40,
                                            color = color.purple,
                                            x = games.screen.width/2,
                                            y = games.screen.height/2,
                                            lifetime = 2 * games.screen.fps,
                                            after_death = games.screen.quit)
            games.screen.add(victory_message)
            for obj in games.screen._objects:
                if obj.dy:
                    obj.destroy()




class Rock(games.Sprite):
    """Fabric for create rocks"""
    rock_image = games.load_image('rock.png')
    speed = 3
    def __init__(self, x, y = -100):
        super().__init__(Rock.rock_image,
                         x = x,
                         y = y,
                         dy = Rock.speed)



class Crumbing_Temple(games.Sprite):
    """Create rock falling on head gg"""
    image = games.load_image('crumb_temple.jpg')
    def __init__(self, gg):
        super().__init__(Crumbing_Temple.image, x = games.screen.width/2,
                         y = -100)
        self.time_drop = 0
        self.gg = gg


    def update(self):
        if self.time_drop > 0:
            self.time_drop -= 1
        else:
            self.x = r.randint(20,620) #Протести значения 0 и 640 # Падает ровно по краю
            self.drop_rock()
            self.increase_score()

    def drop_rock(self):
        rock = Rock(x = self.x)
        games.screen.add(rock)
        self.time_drop = 35


    def increase_score(self):
        """Check tap rock bottom and increase points"""
        for rock in games.screen._objects:
            if rock.dy:
                if rock.bottom >= games.screen.height:
                    self.gg.score.value -= 10
                    rock.destroy()
                    # Как сделать так чтобы персонаж не двигался?
                    # Как минимум реализовать эту возможность в классе персонажа)




def main():
    background_image = games.load_image('temple.bmp', transparent = False)
    games.screen.background = background_image
    gg = GG()
    games.screen.add(gg)
    crumb_temple = Crumbing_Temple(gg)
    games.screen.add(crumb_temple)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()