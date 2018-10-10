class Player():
    """Player in action-game"""
    def blast(self, enemy):
        print('Player shoot in enemy.\n')
        enemy.die()

class Alien():
    """Warning alien in action game"""
    def die(self):
        print('I die.')

hero = Player()
invader = Alien()
hero.blast(invader)
