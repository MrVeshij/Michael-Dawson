from livewires import games

games.init()
missile_sound = games.load_sound('missile.wav')
games.music.load('theme.mid')

choice = None
while choice != '0':
    print(
        """
        Sound and music
        0 - Exit
        1 - Play sound missile salvo
        2 - Cycle sound missile salvo
        3 - Stop sound missile salvo
        4 - Play music theme game
        5 - Cycle music them game
        6 - Stop music theme game
        """
    )
    choice = input('Your choice: ')
    print()
    if choice =='0':
        print('Goodbye.')
    elif choice == '1':
        missile_sound.play()
        print('Reproduce sound missile salvo')
    elif choice == '2':
        loop = int(input('How much reproduce that sound? '
                         '(-1 = reproduce never stop): '))
        missile_sound.play(loop)
        print('Cycle sound missile salvo.')
    elif choice == '3':
        missile_sound.stop()
        print('Stop sound missile salvo.')
    elif choice == '4':
        games.music.play()
        print('Reproduce music game theme.')
    elif choice == '5':
        loop = int(input('How much reproduce that music?'
                         '(-1 = reproduce never stop): '))
        games.music.play(loop)
        print('Cycle music game theme')
    elif choice == '6':
        games.music.stop()
        print('Stop music game theme.')
    else:
        print('Sorry, menu hasn\'t that choice.')

input('\n\nPress Enter for exit.')

