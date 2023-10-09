import pygame

class Sprite():
    def __init__(self, pos, surface):
        self.rect = surface.get_rect(topleft=pos)
        self.surface = surface
