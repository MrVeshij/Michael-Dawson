#Доработайте игру «Паника в пиццерии» так, чтобы сложность игрового nроцесса постепенно возрастала.
#Задумайтесь о разных способах добиться сnедующих эффектов: увеличить скорость падения пиццы и/или перемещения
#повара, уменьшить расстояние от крыши до сковороды, наконец, выпустить на экран нескольких
#сумасшедших кулинаров.

from livewires import games, color
import random
games.init(screen_width=640, screen_height=480, fps=50)

class Pan(games.Sprite):
    image = games.load_image("pan.bmp")
    def __init__(self, chef):
        super(Pan, self).__init__(image = Pan.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        self.chef = chef
        games.screen.add(self.score)
    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()
    def check_catch(self):
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pizza.handle_caught()
            if self.score.value in range(100, 1000, 100):
                pizza.speed_up()
            if self.score.value == 400:
                self.chef.speed_change()
            if self.score.value == 100:
                self.chef.add_chef()



class Pizza(games.Sprite):
    image = games.load_image("pizza.bmp")
    speed = 1
    def __init__(self, x, y = 90):
        super(Pizza, self).__init__(image = Pizza.image,
                                    x = x, y = y,
                                    dy = Pizza.speed)
    def update(self):
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
    def handle_caught(self):
        self.destroy()
    def speed_up(self):
        Pizza.speed += 0.2
    def end_game(self):
        end_message = games.Message(value = "Game over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)


class Chef(games.Sprite):
    image = games.load_image("chef.bmp")
    def __init__(self, y = 55, speed = 2, odds_change = 200):
        super(Chef, self).__init__(image = Chef.image,
                                   x = games.screen.width/2,
                                   y = y,
                                   dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0
    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()
    def speed_change(self):
        self.odds_change -= 100
    def add_chef(self):
        the_chef_2 = Chef()
        games.screen.add(the_chef_2)
    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -=1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1


def main():
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image
    the_chef = Chef()
    games.screen.add(the_chef)
    the_pan = Pan(the_chef)
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()















