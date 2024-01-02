from pygame import Surface, Vector2
from objects import sprite

class Bomb():
	"""
	Obstáculo que tira pontos de vida do jogador.

	Argumentos:
	---
	- pos: posição da maça na matriz.
	- surface: superfície na qual imprimir a sprite.
	- damage: dano causado.
	"""

	def __init__(self, pos:Vector2, surface:Surface, damage:int=1):
		self.pos = pos
		self.sprite = sprite.Sprite(pos, surface)
		self.damage = damage
