# 1)Доработайте игру «Паника в пиццерии» так, чтобы сложность игрового процесса постепенно возрастала.
# Задумайтесь о разных способах добиться следующих эффектов: увеличить скорость падения пиццы и/или пе­
# ремещения повара, уменьшить расстояние от крыши до сковороды, наконец, выпустить на экран нескольких
# сумасшедших кулинаров.

# Description:
# - Увеличить скорость падения пиццы
# В первую очередь необходимо создать счетчик отслеживающий состояние счета
# после изменения его параметров, ввести 4 уровня сложности из которых скорость падения пиццы будет первым
# Каждый уровень сложности должен отображаться пользователю
# - Увеличить скорость перемещения повара - изменяем переменную отвечающу за передвижение по абциссе + выводим сообщение о повышение сложности


from livewires import games, color
import random

games.init()




class Pan(games.Sprite):
    """Pan, in whom player will catch fall pizza"""
    image = games.load_image('pan.bmp')
    def __init__(self):
        """init object Pan and create object Text for visual count"""
        super().__init__(image = Pan.image,
                         x = games.mouse.x,
                         bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)


    def update(self):
        """Move object on horizontal in """
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()
        self.difficult()


    def check_catch(self):
        """Check, player catch fall pizza or not"""
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pizza.handle_caught()

    def difficult(self):
        """Correct difficult in game"""
        # level 1, increase speed falling pizza
        if self.score.value == 50:
            lvl_1_msg = games.Message(value = 'Difficult: Level 1',
                          size = 90,
                          color = color.black,
                          x = games.screen.width/2,
                          y = games.screen.height/2,
                          lifetime = 1 * games.screen.fps) # Как работает этот ЕБАННЫЙ атрибут, что это за хогартская магия?????
            # Разобрался, это не хогвартская магия, я погорячился, Карина сможешь разобраться?
            games.screen.add(lvl_1_msg)
            Pizza.speed = 3
        # level 2,
        if self.score.value == 100:
            lvl_2_msg = games.Message(value = 'Difficult: Level 2',
                                      size = 90,
                                      color = color.blue,
                                      x = games.screen.width/2,
                                      y = games.screen.height/2,
                                      lifetime = 1 * games.screen.fps)
            games.screen.add(lvl_2_msg)




class Pizza(games.Sprite):
    """Circle pizza, fall on ground"""
    image = games.load_image('pizza.bmp')
    speed = 1
    def __init__(self, x, y = 90):
        """init object Pizza"""
        super(Pizza, self).__init__(image = Pizza.image,
                                    x = x, y = y,
                                    dy = Pizza.speed)


    def update(self):
        """check tapped pizza border screen or not"""
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()


    def handle_caught(self):
        """Destroy object, catch player"""
        self.destroy()


    def end_game(self):
        """Ending game"""
        end_message = games.Message(value = 'Game Over',
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)



class Chef(games.Sprite):
    """Chef whom throw pizza move left - right"""
    image = games.load_image('chef.bmp')
    def __init__(self, y = 55, speed = 2, odds_change = 200):
        """init object Chef"""
        super().__init__(image = Chef.image,
                         x = games.screen.width/2,
                         y = y,
                         dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0



    def update(self):
        """Defined got change course"""
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()


    def check_drop(self):
        """Reduce interval expectation on one or drop next pizza and recover initial interval"""
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            self.time_til_drop = int(new_pizza.height * 1.3 )
            print(self.time_til_drop)



def main():
    """Game process"""
    wall_image = games.load_image('wall.jpg', transparent = False)
    games.screen.background = wall_image
    the_chef = Chef()
    games.screen.add(the_chef)
    the_pan = Pan()
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()