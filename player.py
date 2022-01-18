import pygame as pg

class Player:
    def __init__(self, image_player, pos_x, pos_y):
        self.image = pg.image.load(image_player).convert_alpha()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 5
        self.new_position_player = self.pos_x
        self.is_colliding_x = False
        self.new_player_rect = pg.Rect(self.new_position_player, self.pos_y, 72, 72)

    def draw(self, window):
        window.blit(self.image, (self.new_position_player, self.pos_y))

    def events_player(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.new_position_player -= self.speed
        elif keys[pg.K_d]:
            self.new_position_player += self.speed

        if not self.is_colliding_x:
            self.pos_x = self.new_position_player
        else:
            print("colliding")

        print(f"collide: {self.is_colliding_x}")
    def movement_player(self):
        self.events_player()

    def update_player(self, window):
        self.draw(window)
        self.movement_player()
