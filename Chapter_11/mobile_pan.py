from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    """Moving mouses pan"""
    def update(self):
        """move object to position pointer"""
        self.x = games.mouse.x
        self.y = games.mouse.y


def main():
    wall_image = games.load_image('wall.jpg', transparent = False)
    games.screen.background = wall_image
    pan_image = games.load_image('pan.bmp')
    the_pan = Pan(image = pan_image, # Именнованый аргумент, зачем?МОжно использовать просто позиционный
                  x = games.mouse.x, # Лишняя строка - эти данные объявленны в классе Pan
                  y = games.mouse.y) # Лишняя строка - эти данные объявленны в классе Pan
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()
