from random import randint
from pygame import Vector2, K_UP, K_DOWN, K_RIGHT, K_LEFT, K_w, K_s, K_d, K_a

from settings import SETTINGS
from objects.segment import Segment


class Snake():
	"""
	Cobrinha.

    Argumentos:
    ---
	- grid_size: largura e altura da grade;
	- unit_size: tamanho da célula;
	- snake_sprites: sprites da cobrinha.
    """

	def __init__(self, grid_size:Vector2, unit_size:int, snake_sprites):
		# Sprites
		self.sprites = {
			"straight": snake_sprites[0],
			"curved": snake_sprites[1],
			"head": snake_sprites[2],
			"tail": snake_sprites[3]
		}

		grid_units = Vector2([int(i) for i in grid_size / unit_size])# (int(grid_size.x / unit_size), int(grid_size[1] / unit_size))

		self.lives = 1
		self.size = 1

		# Head direction & position
		head_pos = Vector2(
			SETTINGS["GRID_ORIGIN"].x + randint(2, grid_units.x - 3) * SETTINGS["UNIT_SIZE"],
			SETTINGS["GRID_ORIGIN"].x + randint(2, grid_units.y - 3) * SETTINGS["UNIT_SIZE"]
		)

		front = randint(0, 3)
		self.move_direction = Vector2(front, 0)

		if front < 2:
			self.move_direction.y = front + 2
		else:
			self.move_direction.y = front - 2

		self.segments = [Segment(head_pos, self.move_direction)]
		self.addSegment()
		#self.addSegment()

	def update(self, input:dict, slow_frame:bool):
		"""
		Atualiza os segmentos da cobrinha.

		Argumentos:
		---
		- input: dicionário com as entradas de interesse;
		- slow_frame: valor que indica se o jogo deve atualizar a cena principal.
		"""
		if K_RIGHT in input["KEYSDOWN"] or K_d in input["KEYSDOWN"]:
			self.move_direction = Vector2(0, 2)
		elif K_DOWN in input["KEYSDOWN"] or K_s in input["KEYSDOWN"]:
			self.move_direction = Vector2(1, 3)
		elif K_LEFT in input["KEYSDOWN"] or K_a in input["KEYSDOWN"]:
			self.move_direction = Vector2(2, 0)
		elif K_UP in input["KEYSDOWN"] or K_w in input["KEYSDOWN"]:
			self.move_direction = Vector2(3, 1)

		if slow_frame:
			if self.move_direction.y != self.segments[0].direction.x:
				self.segments[0].direction = self.move_direction

			self.movement(input)


	def movement(self, input):
		"""
		Movimentação da cobrinha.

		Argumentos:
		---
		- input: dicionário com as entradas de interesse.
		"""
		# Update head
		x = y = 0

		if self.segments[0].direction.y == 0:
			x = -1
		elif self.segments[0].direction.y == 2:
			x = 1
		elif self.segments[0].direction.y == 1:
			y = -1
		else:
			y = 1

		self.segments[0].pos.x += x * SETTINGS["UNIT_SIZE"]
		self.segments[0].pos.y += y * SETTINGS["UNIT_SIZE"]

		# Update body
		for i in range(1, len(self.segments)):
			self.segments[i].pos = self.getUnitBehind(i - 1)

			self.segments[i].direction.x = self.getOppositeDirection(self.segments[i].direction.y)
			self.segments[i].direction.y = self.getOppositeDirection(self.segments[i - 1].direction.x)


	def addSegment(self):
		self.size += 1
		direction = Vector2(self.getOppositeDirection(self.segments[-1].direction.x), self.segments[-1].direction.x)
		self.segments.append(Segment(self.getUnitBehind(), direction))


	def getUnitBehind(self, index=-1):
		x = y = 0

		if self.segments[index].direction.x == 0:
			x = -1
		elif self.segments[index].direction.x == 2:
			x = 1
		elif self.segments[index].direction.x == 1:
			y = -1
		else:
			y = 1

		return Vector2(
			self.segments[index].pos.x + x * SETTINGS["UNIT_SIZE"],
			self.segments[index].pos.y + y * SETTINGS["UNIT_SIZE"]
		)


	def setSnakeSprites(self):
		for i in range(len(self.segments)):
			self.setSegmentRotation(i)

			if i == 0:
				self.segments[0].sprite = "head"

			elif i == len(self.segments) - 1:
				self.segments[-1].sprite = "tail"

			else:
				if abs(self.segments[i].direction.x - self.segments[i].direction.y) != 2:
					self.segments[i].sprite = "curved"
				else:
					self.segments[i].sprite = "straight"


	def setSegmentRotation(self, i):
		direction_difference = abs(self.segments[i].direction.x - self.segments[i].direction.y)
		direction_sum = self.segments[i].direction.x + self.segments[i].direction.y

		rotation = 0

		if direction_difference == 3:
			rotation = 1

		elif direction_difference == 2:
			rotation = range(0, 4)[- self.segments[i].direction.x]

		elif direction_difference == 1:
			if direction_sum == 1:
				rotation = 0
			if direction_sum == 3:
				rotation = 3
			if direction_sum == 5:
				rotation = 2

		self.segments[i].rotation = rotation


	def getOppositeDirection(self, direction:int | float):
		return [2, 3, 0, 1][int(direction)]
