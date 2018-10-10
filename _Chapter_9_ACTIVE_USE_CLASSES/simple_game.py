import games, random
print("Welcome to simple game!\n")
again = None
while again != 'n':
    players = []
    num = games.ask_number(question = 'How much player play? (2-5): ', low = 2, high = 6)
    for i in range(num):
        name = input('Name player: ')
        score = random.randrange(100) + 1
        player = games.Player(name, score)
        players.append(player)
    print('\nIt results games:')
    for player in players:
        print(player)
    again = games.ask_yes_no('\nWould you play agin? (y/n): ')
