# 2)Создайте программу, имитирующую телевизор как объект. У пользователя должна быть возможность вводить
# номер канала, а также увеличивать и уменьшать громкость. Программа допжна следить за тем, чтобы номер
# канала и уровень громкости оставались в допустимых пределах.

# Псевдокод:
# Есть обьект телевизор, который принимает определенное количество
# громковсть может быть не ниже 0 и не выше 100.
# Пользователь может обратитсья к обьекту чтобы узнать уровень громкости и номер канала на котором находится ТВ
# Выход стилизован как выключение ТВ



class TV():
    def __init__(self, channels):
        self.channels = channels
        self.channel = 0
        self.volume = 50

    def change_volume(self, volume = 50):
        if volume > 100 or volume < 0:
            print('Volume not may more or less availibale values.')
        else:
            self.volume = volume
            return self.volume

    def change_step_volume_up(self):
        if self.volume + 1 > 100:
            print('Unacceptable! Volume not may more 100.')
        else:
            self.volume += 1

    def change_step_volume_down(self):
        if self.volume - 1 <= 0:
            print('Unacceptable! Volume not may less 0.')
        else:
            self.volume -= 1

    def change_step_channel_up(self):
        if self.channel >= self.channels:
            print('Unacceptable! Channel not may more', self.channels)
        else:
            self.channel += 1

    def change_step_channel_down(self):
        if self.channel <= 0:
            print('Unacceptable! Channel not may less 0.')
        else:
            self.channel -= 1

    def change_channel(self, channel):
        if channel > self.channels or channel < 0:
            print('That TV haven\'t the channel.')
        else:
            self.channel = channel
            return self.channel

    def info(self):
        print('You stay at channel', self.channel, '.Volume equal', self.volume)

# test
# tv1 = TV(20)
# tv1.info()
# tv1.change_channel(21)
# tv1.change_channel(19)
# tv1.info()

def main_ver1():
    ch_tv = int(input("You buy new TV with 'n' channels, how much channels you have?\n"))
    tv1 = TV(ch_tv)
    choice = None
    while choice != '4':
        print("""
        You turn on TV:
        1 - Look info about channel and volume
        2 - Choice channel
        3 - Choice volume
        4 - turn of tv
        """)
        choice = input('Your choice?\n')
        if choice == '1':
            tv1.info()
        if choice == '2':
            channel = int(input('Input channel.\n'))
            tv1.change_channel(channel)
        if choice == '3':
            volume = int(input('Input volume.\n'))
            tv1.change_volume(volume)
        if choice == '4':
            print('Turn off.')
            break

def main_ver2():
    ch_tv = int(input("You buy old TV with 'n' channels, how much channels you have?\n"))
    tv1 = TV(ch_tv)
    choice = None
    while choice != '6':
        print("""
        You turn on TV:
        1 - Look info about channel and volume
        2 - Change channel by one up
        3 - Change channel by one down
        4 - Change volume by one up
        5 - Change volume by one down
        6 - turn of tv
        """)
        choice = input('Your choice?\n')
        if choice == '1':
            tv1.info()
        if choice == '2':
            tv1.change_step_channel_up()
        if choice == '3':
            tv1.change_step_channel_down()
        if choice == '4':
            tv1.change_step_volume_up()
        if choice == '5':
            tv1.change_step_volume_down()
        if choice == '6':
            print('Turn off.')
            break


#main_ver1()
main_ver2()
