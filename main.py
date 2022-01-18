import pygame as pg
from player import Player
from plataforms import Platform

pg.init()

# constants
SCREEN_SIZE = (700, 400)
GAME_NAME = "DINOSGAME"
BACKGROUND_COLOR = (244, 244, 244)

#variables
clock = pg.time.Clock()
is_running = True
platform_color = (61, 227, 94)

# screen game
window = pg.display.set_mode(SCREEN_SIZE)
game_title = pg.display.set_caption(GAME_NAME)

# characters
# Pos_x e Pos_y são o tamanho da tela divisão inteira por 2 menos metade do tamanho do personagem
player = Player("assets/idle/player_0.png", SCREEN_SIZE[0]//2 - 36, SCREEN_SIZE[1]//2 - 36 + 50)

# platfforms game
platforms = [
    # left
    Platform(100, 300, 400, 50, platform_color),
    # middle
    Platform(100, 250, 50, 50, platform_color),
    # right
    Platform(450, 250, 50, 50, platform_color)
]

# game loop
while is_running:
    window.fill(BACKGROUND_COLOR)

    # events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    # draw space
    player.update_player(window)

    for platform in platforms:
        platform.update_platform(window)

    # dando erro
    if platforms[0].platform_rect.colliderect(player.new_player_rect):
        player.is_colliding_x = True

    pg.display.update()
    clock.tick(60)

pg.quit()