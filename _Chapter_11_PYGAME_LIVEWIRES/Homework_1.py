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
# - Уменьшить расстояние от крыши до сковородки
# - Добавляем 2 поваров.
# Я не могу понять как добавить новые экземпляры класса в программу
# Сталкиваюсь с проблемой отработки fps
# И все проблемы устранены - код в порядке и протестирован - все отлично работает

from livewires import games, color
import random


games.init()


class Pan(games.Sprite):
    """Pan, in whom player will catch fall pizza"""
    image = games.load_image('pan.bmp')
    def __init__(self, the_chef):
        """init object Pan and create object Text for visual count"""
        super().__init__(Pan.image,
                         x = games.mouse.x,
                         bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)
        self.chef = the_chef
        self.time_born = 25
        self.check_speed = 0


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
        if self.score.value == 200:
            lvl_1_msg = games.Message(value = 'Difficult: Level 1',
                          size = 90,
                          color = color.black,
                          x = games.screen.width/2,
                          y = games.screen.height/2,
                          lifetime = 0.5 * games.screen.fps) # Как работает этот ЕБАННЫЙ атрибут, что это за хогартская магия?????
            # Разобрался, это не хогвартская магия, я погорячился, Карина сможешь разобраться?
            games.screen.add(lvl_1_msg)
            Pizza.speed = 2
        # level 2, increase speed chef
        if self.score.value == 400:
            lvl_2_msg = games.Message(value = 'Difficult: Level 2',
                                      size = 90,
                                      color = color.blue,
                                      x = games.screen.width/2,
                                      y = games.screen.height/2,
                                      lifetime = 0.5 * games.screen.fps)
            games.screen.add(lvl_2_msg)
            if not self.check_speed:
                self.chef.dx = 4 # При значение переменной 5, шеф уходит за экран, думаю проблема в исчесления и случайной переменной
                self.check_speed += 1
            # Данное событие происходит редко, поменяв значение на 4 проблемы не наблюдаю
            # Нашел в чем косяк (присваивание не одноразовое)
        # level 3, increase distant pan of wall
        if self.score.value == 600:
            lvl_3_msg = games.Message(value = 'Difficult: Level 3',
                                      size = 90,
                                      color = color.yellow,
                                      x = games.screen.width/2,
                                      y = games.screen.height/2,
                                      lifetime = 0.5 * games.screen.fps)
            games.screen.add(lvl_3_msg)
            self.bottom = 440
        # level 4, add two chefs
        if self.score.value == 800:
            lvl_4_msg = games.Message(value = 'Difficult: Level 4',
                                      size = 90,
                                      color = color.white,
                                      x = games.screen.width/2,
                                      y = games.screen.height/2,
                                      lifetime = 0.5 * games.screen.fps)
            games.screen.add(lvl_4_msg)
            if self.time_born > 0:
                self.time_born -= 1
            else:
                the_chef= Chef(speed = 4)
                games.screen.add(the_chef) # Создаст 50 поваров #fixed
                self.time_born = 26 # При переменной в 25 (чтобы в 1 сек было создано 2 повара) есть вероятность появления от 4 до 5 поваров
                # Предполагаю что проблема замедление при выведения сообщения на экран в момент достижения очков
                # Возможно только в тестовом режими
        # 1000 points = victory
        if self.score.value == 1000:
            victory_message = games.Message(value = 'You obtain 1000 points! Victory!',
                                               size = 60,
                                            color = color.purple,
                                            x = games.screen.width/2,
                                            y = games.screen.height/2,
                                            lifetime = 2 * games.screen.fps,
                                            after_death = games.screen.quit)
            games.screen.add(victory_message)
            for obj in games.screen._objects:
                if obj.dy:
                    obj.destroy()




class Pizza(games.Sprite):
    """Circle pizza, fall on ground"""
    image = games.load_image('pizza.bmp')
    speed = 1
    def __init__(self, x, y = 90):
        """init object Pizza"""
        super(Pizza, self).__init__(image = Pizza.image,
                                    x = x, y = y,
                                    dy = Pizza.speed)
        self.check = 0


    def update(self):
        """check tapped pizza border screen or not"""
        if self.bottom > games.screen.height:
            self.check += 1
            self.end_game()


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
                                    lifetime = 2 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
        for i in range(10): self.destroy_all_pizza()


    def destroy_all_pizza(self):
        """Clear list of pizza but not clear new falling pizza"""
        for obj in games.screen._objects: # Этот перебор останавливает пиццы в воздухе, но через секунду падают новые #Fixed
            if obj.dy:
                if obj.check == 0:
                    obj.destroy()

class Chef(games.Sprite):
    """Chef whom throw pizza move left - right"""
    image = games.load_image('chef.bmp')
    speed = 2
    def __init__(self, y = 55, speed = speed, odds_change = 200):
        """init object Chef"""
        super().__init__(image = Chef.image,
                         x = games.screen.width/2,
                         y = y,
                         dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0



    def update(self):
        """Defined got change course"""
        if self.left < 0 or self.right > games.screen.width: # Если ставить условие на равно, может быть баг что повар застрянет в углу
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



def main():
    """Game process"""
    wall_image = games.load_image('wall.jpg', transparent = False)
    games.screen.background = wall_image
    the_chef = Chef()
    games.screen.add(the_chef)
    the_pan = Pan(the_chef) # объект класса Pan получает доступ к объекту класса Chef
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()
