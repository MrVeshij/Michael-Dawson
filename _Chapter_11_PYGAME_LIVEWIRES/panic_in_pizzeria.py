from livewires import games, color
import random

games.init() # Инициализация экрана, создается переменная screen содержащая класс Screen

class Pan(games.Sprite):
    """Pan, in whom player will catch fall pizza"""
    image = games.load_image('pan.bmp')
    def __init__(self):
        """init object Pan and create object Text for visual count"""
        super().__init__(Pan.image,
                         x = games.mouse.x,
                         bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score) # Добавляет спрайт в список атрибут _objects экземпляра класса Screen - screen


    def update(self): # Метод вызывается в методе mainloop , изначально метод пустой и переписывается по требованию разраба
        """Move object on horizontal in """
        self.x = games.mouse.x # Присваивает переменной x местоположение мыши
        if self.left < 0: # Создается значение self.left = 0 т.к при инициализации left = 0
            self.left = 0
        if self.right > games.screen.width: # Аналогично self.left
            self.right = games.screen.width
        self.check_catch() # Применяется ниже созданная нами функция


    def check_catch(self):
        """Check, player catch fall pizza or not"""
        # Перебирает все объекты которые были столкнуты, меняет переменную self.score.value на + 10 при каждом таком объете
        for pizza in self.overlapping_sprites: # Список всех спрайтов момещенный в атрибут overlapping_objects экземпляра класса Screen
            self.score.value += 10
            #self.score.right = games.screen.width - 10 # Строка отвечает за параметр расположения объекта screen (Уже была обьявлена в методе конструктора)
            pizza.handle_caught()  # объект "уничтожается" - стирается с экрана, сам экземлпяр класса удаляется



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
        if self.bottom > games.screen.height: # Если значение bottom объекта Pizza больше чем высоты экрана (480)
            self.end_game() # Игра заканчивается
            self.destroy() # Объект исчезает


    def handle_caught(self):
        """Destroy object, catch player"""
        self.destroy() # уничтожает себя как объект, удаляя из спсиска self._objects экземпляра screen


    def end_game(self):
        """Ending game"""
        end_message = games.Message(value = 'Game Over',
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps, # Спрайт живет 5 секунд
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
        self.odds_change = odds_change # Шансы на изменение направление движения
        self.time_til_drop = 0



    def update(self):
        """Defined got change course"""
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()  # Сброс пиццы


    def check_drop(self):
        """Reduce interval expectation on one or drop next pizza and recover initial interval"""
        if self.time_til_drop > 0: # Проверяет переменную time_till_drop, если она больше 0
            self.time_til_drop -= 1 # Отнимает от значения 1
        else:
            new_pizza = Pizza(x = self.x) # Иначе создает объект класса pizza, там же где расположен х объекта класса Chef
            games.screen.add(new_pizza) # Добавляет в экземпляр класса Screen экземпляр класса Pizza
            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1 # разница во времени когда пицца будет сброшена (учитываются fps)




def main():
    """Game process"""
    wall_image = games.load_image('wall.jpg', transparent = False) # создаем переменную с фоновым изображением
    games.screen.background = wall_image # Добавляет в атрибут экземпляра класса Screen фоновое изображение
    the_chef = Chef() # объект экземпляра класса Chef
    games.screen.add(the_chef) # Добавляет спрайт
    the_pan = Pan() # объект экземпляра Pan
    games.screen.add(the_pan) # Добавляет спрайт
    games.mouse.is_visible = False # Меняет значение переменной ответственной за видимость мыши
    games.screen.event_grab = True # Меняет значение переменной ответственной за влияние мыши
    games.screen.mainloop() # Петля

main()