import pygame as pg

class Player:
    def __init__(self, image_player, pos_x, pos_y):
        self.image = pg.image.load(image_player).convert_alpha()
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))

    def update_player(self):
        self.draw()