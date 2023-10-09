from objects import sprite

class Apple():
    def __init__(self, pos, surface, points=1):
        self.pos = pos
        self.sprite = sprite.Sprite(pos, surface)
        self.points = points
