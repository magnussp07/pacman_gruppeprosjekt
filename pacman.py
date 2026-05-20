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
        
        self.dir_x = 0
        self.dir_y = 0 
        
        self.frames_idle = self.getImageSpriteList(0, 0, 4)
        # Bildet vi skal vise til å starte med er idle:
        self.frames = self.frames_idle
        # Om vi vil ha animasjon som går gjennom frames:
        self.current_frame = 0

        # Om vi vil speile bildet:
        self.venstre = False
        
    def is_centered(self):
            return (self.x % TILE_SIZE == 0 and self.y % TILE_SIZE == 0)
        
    def update(self, board):
        
        keys = pg.key.get_pressed()
        
        if self.is_centered():
        
            if keys[pg.K_LEFT]:
                self.dir_x = -1
                self.dir_y = 0
                
                self.venstre = True
            
            elif keys[pg.K_RIGHT]:
                self.dir_x = 1 
                self.dir_y = 0
                self.venstre = False
            
            elif keys[pg.K_UP]: 
                self.dir_x = 0 
                self.dir_y = -1 
            
            elif keys[pg.K_DOWN]:
                self.dir_x = 0 
                self.dir_y = 1 
            
        # Beregner neste posisjon
        next_x = self.x + self.dir_x * self.speed
        next_y = self.y + self.dir_y * self.speed

        # Finn hvilken tile vi beveger oss mot
        next_col = next_x // TILE_SIZE
        next_row = next_y // TILE_SIZE

        if self.dir_x > 0:  #høyre bevegelse
                next_col = (next_x + TILE_SIZE - 1) // TILE_SIZE
        elif self.dir_x < 0:  # venstre bevegelse
                next_col = next_x // TILE_SIZE
        else:
                next_col = self.x // TILE_SIZE
            
        if self.dir_y > 0:  # nedover bevegelse
                next_row = (next_y + TILE_SIZE - 1) // TILE_SIZE
        elif self.dir_y < 0:  # oppover vegelse
                next_row = next_y // TILE_SIZE
        else:
                next_row = self.y // TILE_SIZE

            #  om neste tile er gyldig
        if board.is_road(next_col, next_row):
            self.x = next_x
            self.y = next_y
                
                # Oppdater grid-posisjon når  sentrert
            if self.is_centered():
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

