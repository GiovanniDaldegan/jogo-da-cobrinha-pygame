from pygame import Vector2, Surface

class Sprite():
    """
    Argumentos:
    ---
    - pos: posição em pixels;
    - surface: superfície da sprite.
    """

    def __init__(self, pos:Vector2, surface:Surface):
        self.rect = surface.get_rect(topleft=pos)
        self.surface = surface
