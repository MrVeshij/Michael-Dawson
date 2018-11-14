# 2) Напишите вариант детской игры «(Саймон говорит- запоминайте» (Simon Says). В ней игрок должен с клавиа­
# туры дублировать все удлиняющуюся сяучайную последовательность звуков и цветов, которые воспроизводит
# и демонстрирует компьютер.

# Description:
# Version 1
# Открывается окно с нейтральным цветом (белым), посередине стоит человек
# Он произносит слова и показывает цвет например в шаре - эти слова и цвета юзер должен записывать в течение определенного
# времени в текстовую консоль, если время заканчивается - игрок проигрывает и выводится финальный счет на экран
# Игра идет по прогрессии, сначало случайный цвет или слово, потом 2 , 3, 4 итд. Вместе с количеством слов растет и время на ответ
# Время до конца должно выходить слева вверху
# Проблема реализации - я не умею использовать пользовательский ввод. Хотя я могу создать модульный клас для отрисовки все букв
# руского алфавита. Но в таком случае есть проблема - при удлинение последовательности ввода, пользователь будет испытывать проблемы
#при вводе большого колчества строк. Надо реализовать более упрощенную версию где юзер может оперировать максимум 4 кнопками для
#выбора необходимых ему слов\цветов


# Version 2 = Игра разделена на 10 уровней, каждый уровень это количество слов в зависимости от его значения, 7 уровень - 7 слов
# Первый уровень - Саймон говорит - появляется слово, пользователь должен выбрать из 4 вариантов на экране исользуюя стрелочки
# Если пользователь не угадал - игра завершается, если угадал игра переходит на новый уровень где количество слов увеличивается в зависимости
# от уровня

#
# Pseudocode:
# Фон - белый лист
# Персонаж - тип за столом где есть шар
# Описание игры вверху - отменяется вместе с началом игры с помощью ИНТЕР
# Основной модуль игра который проводит сверку на вводимый игроком текст
# Класс спрайтов вызываемых при различных ситуациях



from livewires import games, color
import random

games.init()


class Message_for_game(games.Message):
    def __init__(self, check):
        self.list_words1 = ['wow', 'sprite', 'spam', 'egg', ]
        self.list_words2 = ['one', 'death', 'life', 'exercise',]
        self.list_words3 = ['test1', 'test2', 'test3', 'test4']
        self.list_words4 = ['wizard', 'horn', 'claw', 'butt']
        if check == 1:
            self.rand_word = random.choice(self.list_words1)
        elif check == 0:
            self.rand_word = random.choice(self.list_words2)
        elif check == 2:
            self.rand_word = random.choice(self.list_words3)
        elif check == 3:
            self.rand_word = random.choice(self.list_words4)

        super().__init__(value = 'Simon says: ' + self.rand_word,
                         size = 50,
                         color = color.black,
                         x = games.screen.width/2,
                         y = games.screen.height/2,
                         lifetime = 0.5 * games.screen.fps)


class Control(games.Sprite):
    image_control = games.load_image('ship.bmp')
    def __init__(self):
        self.delay = 10
        super().__init__(image = Control.image_control)


    def update(self): # Настроить работу модуля (проблема - некоректно отображаются надписи, задержки и ускорения появления)
        if games.keyboard.is_pressed(games.K_LEFT):
            if self.delay <= 11:
                self.delay -= 1
                #print(self.delay) # test
            if self.delay == 0:
                self.delay = 11
                inscription = Message_for_game(1)
                games.screen.add(inscription)
        if games.keyboard.is_pressed(games.K_RIGHT):
            if self.delay <= 11:
                self.delay -= 1
            if self.delay == 0:
                self.delay = 11
                inscription = Message_for_game(0)
                games.screen.add(inscription)
        if games.keyboard.is_pressed(games.K_UP):
            if self.delay <= 11:
                self.delay -= 1
            if self.delay == 0:
                self.delay = 11
                inscription = Message_for_game(2)
                games.screen.add(inscription)
        if games.keyboard.is_pressed(games.K_DOWN):
            if self.delay <= 11:
                self.delay -= 1
            if self.delay == 0:
                self.delay = 11
                inscription = Message_for_game(3)
                games.screen.add(inscription)



def main():
    game_fone = games.load_image('white_fone1.jpg', transparent = False) # Если переменная transparent Не будет false игра будет считать белый
    # фон прозрачным и просвечивать через него нутро "оболочки" черный фон.
    games.screen.background = game_fone
    #print('test') # test
    object_control = Control()
    games.screen.add(object_control)
    #print('test2') # test
    games.screen.mainloop()

main()