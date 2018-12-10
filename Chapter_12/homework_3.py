# 3) Напишите свою версию какой-либо другой знаменитой видеоигры, например «Космических захватчиков» или
# «Пакмана».

# Description:
# Написать игру Бомберман, логика игры следующая:
# Есть главный персонаж который имеет способность выкидывать бомбу, бомба падает перед ГГ. У героя есть 3 жизни.
# Задача в игре это прохождение уровня, на уровне находится дверь и ключ от двери.
# Весь уровень состоит из множества блоков, часть из которых неуничтожимые. Остальные можно взорвать
# 1 - 3 уровень врагов нет. 4 - 6 враги с возрастанием на один. 6 - 9 уровень врагов с 4 до 8
# 10 уровень заключительный - босс
# На уровне под блоками кроме выхода и ключа есть бонусы для бомб и на 3 уровнях дополнительно есть по 1 жизни
# Бонусы для бомб увеличивают дальность взрыва и сокращают время на взрыв, первоначально 3 секунды.

# Resources:
# Задник, для каждой главы (1-3 уровня) задан свой задник (Луг, пустыня, космос)
# Блоки - 2 картинки - которые можно взорвать и невзрываемые
# ГГ, картинка бомб, анимация взрыва, таймер для отсчета до взрыва


# LevelDesign:
# Расположение блоков не должно быть рандомное, для каждого уровня должны быть установлены
# списки блоков которые нельзя уничтожить, они должны создавать лабиринт


# Pseudocode:
# Класс ГГ - он вызывает бомбу, при пересечения с врагами - смерть или отнимается жизнь
# Класс Бомба - атрибуты дальности взрыва + мощность + таймер взрыва
# Класс Враг - Логика движения
# Окружение, класс Блока - расположение блоков,
# Класс Босс - ...


from livewires import games, color

games.init()


class Hero(games.Sprite):
    """Main hero, may move up, down, left, right, drop bomb, catch stuff(key, improvements), if
     hero go in door, level up. If hero meets enemy, he lost one life, if life < 0 - game over"""
    hero_image = games.load_image('bomberman/Hero_4.bmp')
    def __init__(self):
        super().__init__(image=Hero.hero_image, x=games.screen.width/2, y=games.screen.height/2)


    def update(self):
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1

        if self.x > games.screen.width - 30:
            self.x = games.screen.width - 30
        if self.x < 30:
            self.x = 30
        if self.y > games.screen.height - 30:
            self.y = games.screen.height - 30
        if self.y < 30:
            self.y = 30

        self.drop_bomb()


    def drop_bomb(self):
        if games.keyboard.is_pressed(games.K_SPACE):
            bomb = Bomb(x=self.x, y=self.y)
            games.screen.add(bomb)


class Enemy(games.Sprite):
    pass



class Block(games.Sprite):
    pass



class Bomb(games.Sprite):
    image = games.load_image('bomberman/bomb_1.jpg')
    def __init__(self, x, y):
        super().__init__(image=Bomb.image, x=x, y=y)
        self.time_life = 50

    def update(self):
        if self.time_life > 0:
            self.time_life -= 1
        else:
            self.destroy()





class Boss(games.Sprite):
    pass





def main():
    background = games.load_image('bomberman/fone_grass(1_3).jpg', transparent=False)
    games.screen.background = background
    hero = Hero()
    games.screen.add(hero)
    games.screen.mainloop()

main()