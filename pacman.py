from pathlib import Path
import pygame as pg
from constants import *

class PacMan:
    IMAGE_FILE = Path(__file__).parent / "sprites" / "pacman2.png"

    def getImageSpriteList(self, x_start, y_start, num_frames) -> list[pg.Surface]:
        full_image = pg.image.load(self.IMAGE_FILE)
        frame_width = 16
        
        # Dele opp bildet i frames, som lagres i en liste:
        frames = []
        for i in range(num_frames):
            # Bildene er kvadratiske - bruker frame widht både som høye og bredde:
            frame = full_image.subsurface(pg.Rect(x_start + i * frame_width, y_start, frame_width, frame_width))
            frames.append(frame)
        return frames
    

    def __init__(self, row, col):
        self.row = row
        self.col = col

        
        self.x = col * TILE_SIZE
        self.y = row * TILE_SIZE
        
        self.speed = 2
        
        self.dx = 0
        self.dy = 0
        
        self.frames_idle = self.getImageSpriteList(0, 0, 4)
        # Bildet vi skal vise til å starte med er idle:
        self.frames = self.frames_idle
        # Om vi vil ha animasjon som går gjennom frames:
        self.current_frame = 0

        # Om vi vil speile bildet:
        self.venstre = False
        
    def update(self, board):
        
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT]:
            self.dx = -self.speed
            self.dy = 0
            self.venstre = True
        
        elif keys[pg.K_RIGHT]:
            self.dx = self.speed
            self.dy = 0
            self.venstre = False
        
        elif keys[pg.K_UP]: 
            self.dx = 0
            self.dy = - self.speed
        
        elif keys[pg.K_DOWN]:
            self.dx = 0
            self.dy = self.speed
            
        next_x = self.x + self.dx
        next_y = self.y + self.dy
        
        next_col = (next_x + TILE_SIZE // 2) // TILE_SIZE
        next_row = (next_y + TILE_SIZE // 2) // TILE_SIZE
        
        if board.is_road(next_col, next_row):
            self.x = next_x
            self.y = next_y
        
        self.col = self.x // TILE_SIZE
        self.row = self.y // TILE_SIZE
    

    def draw(self, surface):

        # Få bildet fra en liste av bilder (om du vil bruke animasjon/sprites):
        current_frame_image = self.frames[self.current_frame]
        
        # Speiler bildet hvis det trengs:
        if self.venstre:
            current_frame_image = pg.transform.flip(
            current_frame_image,
            True,
            False
        )

        # Sørg for at vi tegner midt i "Tile":
        mid = TILE_SIZE // 2
        rect = current_frame_image.get_rect()
        rect.center = (self.x + mid, self.y + mid)
        # Blit images på skjermen (der self.rect befinner seg):
        surface.blit(current_frame_image, rect)

