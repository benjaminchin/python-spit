import pygame as pg
from settings import *

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.spritesheet = pg.image.load(filename).convert()

    def get_sprite(self, x, y, w, h):
        sprite = pg.Surface((w, h))
        # sprite.set_colorkey(BLACK)
        sprite.blit(self.spritesheet, (0, 0), (x, y, w, h))
        return sprite
        