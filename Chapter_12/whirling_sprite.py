from livewires import games

games.init()

class Ship(games.Sprite):
    """Spin ship special image, in due pushed button"""
    def update(self):
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1
        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270

def main():
    nebula_image = games.load_image('nebula.jpg', transparent = False)
    games.screen.background = nebula_image
    ship_image = games.load_image('ship.bmp')
    the_ship = Ship(ship_image,
                    x = games.screen.width/2,
                    y = games.screen.height/2)
    games.screen.add(the_ship)
    games.screen.mainloop()


main()