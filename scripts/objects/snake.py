from random import randint
from objects.segment import Segment


class Snake():
	def __init__(self, grid_origin, grid_size, unit_size, game_sprites):
		# Sprites
		self.sprites = {
			"straight": game_sprites[0],
			"curved": game_sprites[1],
			"head": game_sprites[2],
			"tail": game_sprites[3]
		}

		grid_units = (int(grid_size[0] / unit_size), int(grid_size[1] / unit_size))

		self.lives = 2
		self.size = 1


		# Head direction & position
		head_pos = [randint(2, grid_units[0] - 3), randint(2, grid_units[1] - 3)]

		front = randint(0, 3)
		head_direction = [front, 0]

		if front < 2:
			head_direction[1] = front + 2
		else:
			head_direction[1] = front - 2

		self.segments = [Segment(head_pos, head_direction)]
		self.addSegment()
		self.addSegment()


	def update(self):
		x = y = 0

		# Update head
		if self.segments[0].direction[1] == 0:
			x = -1
		elif self.segments[0].direction[1] == 2:
			x = 1
		elif self.segments[0].direction[1] == 1:
			y = -1
		else:
			y = 1

		self.segments[0].pos[0] += x
		self.segments[0].pos[1] += y

		for i in range(1, len(self.segments)):
			self.segments[i].pos = self.getUnitBehind(i - 1)
			self.segments[i].direction = self.segments[i - 1].direction


	def addSegment(self):
		self.size += 1
		self.segments.append(Segment(self.getUnitBehind(), self.segments[-1].direction))


	def getUnitBehind(self, index=-1):
		x = y = 0

		if self.segments[index].direction[0] == 0:
			x = -1
		elif self.segments[index].direction[0] == 2:
			x = 1
		elif self.segments[index].direction[0] == 1:
			y = -1
		else:
			y = 1

		return [ self.segments[index].pos[0] + x, self.segments[index].pos[1] + y ]
