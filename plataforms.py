import pygame as pg

class Platform:
    def __init__(self, pos_x, pos_y, size_x, size_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.platform_rect = pg.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y)

    def draw(self, window):
        platform = pg.draw.rect(window, self.color, self.platform_rect)

    def update_platform(self, window):
        self.draw(window)