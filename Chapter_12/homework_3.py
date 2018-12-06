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




def main():
    games.init()
    s = games.load_image('nebula.jpg')
    games.screen.background = s
    games.screen.mainloop()

main()