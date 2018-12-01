# 3)Создайте простую игру в пинг-понг для одного игрока. В этой игре пользователь должен манипулировать
# ракеткой, а шарик - отскакивать от трех стенок. Если шарик проскочит мимо ракетки и вылетит за пределы
# игрового поля, игра должна заканчиваться.

# Description:
# Экран имеет 4 стенки, правая стенка отведена под ракетку
# Шарик летит и врезается в ракетку отскакивая в противоположном направлении
# Если шарик пролетае мимо ракетки - игра заканчивается
# В этой игре нету уровней сложности и счета, вся сложность в регулировке угла наклона для шарика
# Вариант запуск шарика не с прямой точки а под наклоном, это приведет к сетке наклонный перемещений
#
#
# Pseudocode:
# Класс ракетка, выводит платформу которой манипулирует игрок, находится на правой стенке экрана
# Класс шарик, имеет внутреннюю смену вектора направления при соприкосновении со стенкой
# Background - фон тенисного корта

#Проблема, как реализовать естественное движение мячика, на данный момент он затыкается среди 2 стенок

from livewires import games, color

games.init()

class Rocket(games.Sprite):
    image = games.load_image('rocket.bmp')
    def __init__(self):
        super().__init__(Rocket.image,
                         right = games.screen.width - 5,
                         y = games.mouse.y)


    def update(self):
        self.y = games.mouse.y
        self.strike_ball()


    def strike_ball(self):
        """Beats ball backwards"""
        for ball in self.overlapping_sprites:
            ball.dx = -ball.dx
            ball.dy = ball.dy




class Ball(games.Sprite):
    image = games.load_image('ball.bmp')
    def __init__(self):
        self.count = 0
        super().__init__(Ball.image,
                         x = 50,
                         y = 320,
                         dx = 2,
                         dy = 2)


    def update(self):
        self.check_walls()
        if self.count in range(0, 10000, 100):
            self.increase_difficult()
        self.count += 1


    def check_walls(self):
        """Check fall ball on wall and change his course"""
        if self.bottom >= games.screen.height:
            self.dx = self.dx
            self.dy = -self.dy
        if self.left <= 0:
            self.dx = -self.dx
            self.dy = self.dy
        if self.top <= 0:
            self.dx = self.dx
            self.dy = -self.dy
        if self.right > games.screen.width + 50:
            self.game_over()


    def increase_difficult(self):
        """Increase speed ball"""
        if self.dx < 0:
            self.dx -= 0.1
        else:
            self.dx += 0.1

        if self.dy < 0:
            self.dy -= 0.1
        else:
            self.dy += 0.1
        print('speed dx',self.dx,'speed dy',self.dy)


    def game_over(self):
        """Declares gameover"""
        gameover = games.Message(value = 'Game Over',
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 2 * games.screen.fps, # Спрайт живет 5 секунд
                                    after_death = games.screen.quit)
        games.screen.add(gameover)


def main():
    image = games.load_image('court.bmp', transparent = False)
    games.screen.background = image
    rocket = Rocket()
    games.screen.add(rocket)
    ball = Ball()
    games.screen.add(ball)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()


main()
