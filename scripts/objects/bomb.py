from objects import sprite

class Bomb():
    def __init__(self, pos, surface, damage=1):
        self.pos = pos
        self.sprite = sprite.Sprite(pos, surface)
        self.damage = damage
