import random, math
from livewires import games, color

games.init()

# Разобрать код по полочкам

class Wrapper(games.Sprite): # Этот класс перенос объект с края экрана на новый край
    # Особенность в системе координат,что top == bottom, left == right с отличием в примерно 50 единиц
    # Эта часть кода меня смутила, я разбирал и тестил ее отдельно
    """Refractoring codes"""
    def update(self): # каждое обновление экрана проверяет нижеуказанную логику
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.right = games.screen.width


    def die(self): # уничтожает объект
        """Destroy object"""
        self.destroy()



class Collider(Wrapper): # Данный класс использует спсок overlapping_sprites
    """Refractoring code"""
    def update(self): #
        super().update() # Испольуется метод обхода из предка Wrapper. Collider является наследуемым классом
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites: # Логика формирования объектов в данном списке следующая:
                # Когда объект класса Collider столкнется с другим объектом других классов, это объект попадает в список
                # overlapping_sprites, Все дальнейшие действия выполняются с ним
                sprite.die() # От астероида нет взрыва, он просто стирается
            self.die()


    def die(self): # Используется анимационный класс демонстрирующий взрыв
        """Destroy object with explosion"""
        new_explosion = Explosion(x = self.x, y =self.y)
        games.screen.add(new_explosion)
        self.destroy()


class Asteroid(Wrapper): # Класс астероид наследуется от класса Wrapper который позволяет огибать экран
    """Asteroid, moving straight on screen"""
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image('asteroid_small.bmp'),
             MEDIUM: games.load_image('asteroid_med.bmp'),
             LARGE: games.load_image('asteroid_big.bmp')}
    SPEED = 2 # Скорость в идеале
    SPAWN = 2 # Количество деления
    POINTS = 30 # Очки за астероид в идеале
    total = 0 # Общее количестов астероидов
    def __init__(self, game, x, y, size): # game - Это экз Game, x и y - это местоположение, size - число от 1 до 3, это размер астероида
        """init sprite with image asteroid"""
        super().__init__(
            image = Asteroid.images[size], # Задается картинка астероида
            x = x, y = y,
            dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size, # Определяется скорость движения по абцисее (чем больше астероид тем медленне он будет двигаться)
            dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size # Определяется скорость движения по ординате
        )
        self.size = size
        Asteroid.total += 1 # При создании экземпляра класса астероида, общая переменная класса увеличивается на 1
        self.game = game


    def die(self): # В случае применения к экземпляру класса Asteroid:
        """Destroy asteroid and replace some asteroid on 2 less"""
        if self.size != Asteroid.SMALL: # Проверка на размер, если размер не равен 1
            for i in range(Asteroid.SPAWN): # Создаются 2 новых объекта на месте уничтожения астероида с размером меньшим на 1
                new_asteroid = Asteroid(game = self.game, x = self.x,
                                        y = self.y,
                                        size = self.size - 1)
                games.screen.add(new_asteroid)
        Asteroid.total -= 1 # При "Смерти" астероида от общего пула созданных астероидов отнимается 1
        self.game.score.value += int(Asteroid.POINTS / self.size) # В переменную счета прибавляется значение погибшегов астероида / на размер астероида
        #self.game.score.right = games.screen.width - 10 # Зачем эта строчка? УДалить проверить//дублирующая строка, расположение счета задано в конструкторе класса Game
        if Asteroid.total == 0: # сначала астероид 1, при смерти создается еще 2, в итоге 3. Потом удаляется погибший, остается 2, и так вплоть до 0
            self.game.advance() # Запуск метода
        super().die()




class Ship(Collider): # При создании объекта Ship
    """Player ship"""
    image = games.load_image('ship.bmp') # Загружаем изображение корабля
    ROTATION_STEP = 3 # Угол отклонения корабля
    VELOCITY_STEP = .03 # шаг увеличения скорости
    sound = games.load_sound('thrust.wav') # Загрузка звука рева двигателя
    MISSILE_DELAY = 25 # Задержка выпуска ракеты
    VELOCITY_MAX = 3 # Максимальная скорость корабля
    def __init__(self, game, x, y): # Корабль респится строго посередине
        """Init sprite with image space ship"""
        super().__init__(Ship.image, x = x, y = y) # Загрузка данных
        self.missile_wait = 0 # Задержка ожидания ракеты
        self.game = game # Передаем ссылку на экз класса Game


    def update(self):
        """Whirl ship by pressing buttons with arrow"""
        super().update() # Проверка на границы, на столкновения
        if games.keyboard.is_pressed(games.K_LEFT): # Угол наклона
            self.angle -= Ship.ROTATION_STEP # -3
        if games.keyboard.is_pressed(games.K_RIGHT): # Угол наклона
            self.angle += Ship.ROTATION_STEP # +3
        if games.keyboard.is_pressed(games.K_UP): # При нажатие вверха увеличивается скорость
            Ship.sound.play() # Проигрывается звук двигателя
            angle = self.angle * math.pi / 180 # Высчитывается угол
            self.dx += Ship.VELOCITY_STEP * math.sin(angle) # Прибавка скорости по абциссе
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle) # Прибавка скорости по ординате
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0: # Если нажат пробел и задержка ракет равна 0
            new_missile = Missile(self.x, self.y,self.angle) # Создается новая ракета, в нее передаются параметры абциссы, ординаты и угла
            games.screen.add(new_missile) # спрайт выводится на экран
            self.missile_wait = Ship.MISSILE_DELAY # обновляется время ожидания новой ракет, выставляется в 25 кадров
        if self.missile_wait > 0: # если задержка больше 0
            self.missile_wait -= 1 # из задержки вычитается 1
        self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX) #Мин(Макс(тек.скорость абциссы, отр. макс скорость), макс.скорость)
        # Ограничение движения, максимальная скорость 3
        self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX) #Мин(Макс(тек.скорость ординаты, отр. макс скорость), макс.скорость)
        # Ограничение движения, максимальная скорость 3

    def die(self): # Вызывает спрайт с концом игры, взрывает корабль
        self.game.end()
        super().die()



class Missile(Collider): # Класс ракет
    """Rocket, which may shoot space ship player"""
    image = games.load_image('missile.bmp') # Загрузка изображения ракет
    sound = games.load_sound('missile.wav') # Загружаем звук
    BUFFER = 40 # растояние в пикселях появления ракеты
    VELOCITY_FACTOR = 7 # скорость движения ракеты
    LIFETIME = 40 # время в кадрах жизни ракеты
    def __init__(self, ship_x, ship_y, ship_angle): # Передаются параметры от корабля
        """Init sprite with image missile"""
        Missile.sound.play() # проигрывается звук запуска ракет
        angle = ship_angle * math.pi / 180 # Высчитывается угол сопоставимый с отметкой на корабле
        buffer_x = Missile.BUFFER * math.sin(angle) # Высчитывается точка появления ракеты по абциссе в 40 писселях от корабля
        buffer_y = Missile.BUFFER * -math.cos(angle) # Высчитывается точка появления ракеты по ординате в 40 писселях от корабля
        x = ship_x + buffer_x # Высчитывается точка появления ракеты по абциссе в 40 писселях от корабля
        y = ship_y + buffer_y # Высчитывается точка появления ракеты по ординате в 40 писселях от корабля
        dx = Missile.VELOCITY_FACTOR * math.sin(angle) # Задается скорость ракеты по абцисе
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle) # Задается скорость ракеты по ординате
        super().__init__(Missile.image, x = x, y = y, # Хер поймешь зачем такие сложные высчеты, надо разбираться в начальной математике
                         dx = dx, dy = dy) #
        self.lifetime = Missile.LIFETIME #


    def update(self):
        """Moves rocket"""
        super().update() # Наследование от Collider ( 1 - переход при попадание на край экрана
        # 2 - проверка на столкновения с другими объектами (астероидами)
        self.lifetime -= 1 # при каждом кадре жизнь выстрела становится меньше на 1
        if self.lifetime == 0: # Если она равна 1:
            self.destroy() # выстрел уничтожается




class Explosion(games.Animation): # Анимация взрыа
    """Animation explosion"""
    sound = games.load_sound('explosion.wav') # Звук взрыва
    images = ['explosion1.bmp',
              'explosion2.bmp',
              'explosion3.bmp',
              'explosion4.bmp',
              'explosion5.bmp',
              'explosion6.bmp',
              'explosion7.bmp',
              'explosion8.bmp',
              'explosion9.bmp',]
    def __init__(self, x, y):
        super().__init__(Explosion.images,
                         x = x, y = y,
                         repeat_interval = 4, n_repeats = 1,
                         is_collideable = False)
        Explosion.sound.play() # После анимации взрыва вызывается звук



class Game():
    """Itself game"""
    def __init__(self):
        self.level = 0 # задается начальный уровень
        self.sound = games.load_sound('level.wav') # Загружается звук повышения уровня
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score) # Игровой счет
        self.ship = Ship(game = self,# В объект экземпляра Ship передается ссылка на объект класса game
                         x = games.screen.width/2,
                         y = games.screen.height/2)
        games.screen.add(self.ship) # Создается корабль как спрайт по центру экрана


    def play(self): # Метод запускающий игру
        games.music.load('theme.mid') # Загружает в память музыку
        games.music.play(-1) # Начинает ее проигрывать
        nebula_image = games.load_image('nebula.jpg') # Создает фон
        games.screen.background = nebula_image # Загружает фон
        self.advance() # Толкает игру на уровень 1 , создается астероид, на экране появляется надпись о первом уровне
        games.screen.mainloop()


    def advance(self): # Продвижение на новый уровень
        self.level += 1 # При запуске прибавляет к переменной уровень 1
        BUFFER = 150
        for i in range(self.level): # В зависимости от уровня
            x_min = random.randrange(BUFFER) # Принимает значение от 0 до 150
            #print('x_min: ', x_min)
            y_min = random.randrange(BUFFER)#BUFFER - x_min # Принимает значение от 0 до 150, нахуя? Почему бы не использовать вышеуказанный вариант? Может из за простоты? # Поменял на свой
            #print('y_min: ', y_min)
            x_distance = random.randrange(x_min, games.screen.width - x_min) # Место появления по абциссе 0 - 640, 150 - 490
            #print('x_distance: ', x_distance)
            y_distance = random.randrange(y_min, games.screen.height - y_min) # Место появления по ординате минимум 0 - 640, 150 - 490
            #print('y_distance: ', y_distance)
            x = self.ship.x + x_distance # 320 + (0 - 640 or 150 - 490)
            #print('self.ship.x: ', self.ship.x)
            #print('x1: ',x)
            y = self.ship.y + y_distance # 240 + (0 - 480 or 150 - 330)
            #print('self.ship.y: ', self.ship.y)
            #print('y1: ',y)
            x %= games.screen.width # Обеспечивает нужное отдаление появляющегося астероида(ов) по оси абциссы
            #print('games.screen.width: ', games.screen.width)
            #print('x2: ', x)
            y %= games.screen.height #Обеспечивает нужное отдаление появляющегося астероида(ов) по оси ординат
            #print('games.screen.height: ', games.screen.height)
            #print('y2: ', y)
            new_asteroid = Asteroid(game = self,
                                    x = x, y = y,
                                    size = Asteroid.LARGE)
            games.screen.add(new_asteroid)
        level_message = games.Message(value = 'Level ' + str(self.level), # Сообщение о следующем уровне
                                      size = 40,
                                      color = color.yellow,
                                      x = games.screen.width/2,
                                      y = games.screen.width/10,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)
        if self.level > 1:
            self.sound.play()


    def end(self): # Вызывает спрайт конца игры
        end_message = games.Message(value = 'Game Over',
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)



def main():
    astrocrash = Game()
    astrocrash.play()


main()
