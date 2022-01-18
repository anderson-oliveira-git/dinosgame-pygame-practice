import pygame as pg
from player import Player

pg.init()

# constants
SCREEN_SIZE = (700, 400)
GAME_NAME = "DINOSGAME"
BACKGROUND_COLOR = (244, 244, 244)

#variables
clock = pg.time.Clock()
is_running = True

# screen game
window = pg.display.set_mode(SCREEN_SIZE)
game_title = pg.display.set_caption(GAME_NAME)

# characters
# Pos_x e Pos_y são o tamanho da tela divisão inteira por 2 menos metade do tamanho do personagem
player = Player("assets/idle/player_0.png", SCREEN_SIZE[0]//2 - 36, SCREEN_SIZE[1]//2 - 36)

# game loop
while is_running:
    window.fill(BACKGROUND_COLOR)

    # events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    # draw space
    player.draw(window)

    pg.display.update()

pg.quit()