from pygame import Surface, Vector2
from objects import sprite

class Apple():
    """
    Item coletável que dá pontos ao jogador.

    Argumentos:
    ---
    - pos: posição da maça na matriz.
    - surface: superfície na qual imprimir a sprite.
    - points: pontuação pela coleta.
    """
    
    def __init__(self, pos:Vector2, surface:Surface, points:int=1):
        self.pos = pos
        self.sprite = sprite.Sprite(pos, surface)
        self.points = points
