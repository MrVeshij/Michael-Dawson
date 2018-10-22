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



class Ball(games.Sprite):
    image = games.load_image('ball.bmp')
    def __init__(self):
        super().__init__(Ball.image,
                         x = 50,
                         y = 320,
                         dx = 1,
                         dy = 1)


    def update(self):
        self.check_walls()


    def check_walls(self):
        """Check fall ball on wall and change his course"""
        if self.bottom >= games.screen.height:
            self.dx = -self.dx
            self.dy = -self.dy
        if self.left <= 0:
            self.dx = -self.dx
            self.dy = -self.dy
        if self.top <= 0:
            self.dx = -self.dx
            self.dy = -self.dy



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