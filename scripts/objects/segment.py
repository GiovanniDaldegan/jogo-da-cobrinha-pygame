from pygame import Vector2

class Segment():
	"""
	Segmento da cobrinha.

    Argumentos:
    ---
	- pos: posição na matriz;
	- direction: direção do segmento (de onde veio e pra onde vai).
    """

	def __init__(self, pos:Vector2, direction:Vector2):
		self.pos = pos
		self.direction = direction
		self.sprite = ""
		self.rotation = 0
