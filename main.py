import pygame as pg
from constants import *
from board import Board
from pacman import PacMan
from ghosts import *

pg.init()
board = Board()
vindu = pg.display.set_mode(board.window_size())
clock = pg.time.Clock()


pacman = PacMan(3, 4)
pinky = Ghost(3,5, 0, 5)
blinky = Ghost(3, 7, 0, 4)
inky = Ghost(3,9,0,6)
clyde = Ghost(3,11,0,7)

objects = (pacman, pinky, blinky, inky, clyde)


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    # Tegn bakgrunn: (En slags "reset" av hele vinduet vårt)
    vindu.fill(BLACK)

    # Tegn brettet først, og pacman og andre ting "oppå":
    board.draw(vindu)

    # TODO: Oppdater objektene våre:


    # Tegn objektene våre:
    for obj in objects:
        obj.draw(vindu)
    pacman.draw(vindu)
    pacman.update(board)


    # Har alltid disse med til slutt:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame på en "ryddig måte":
pg.quit()
