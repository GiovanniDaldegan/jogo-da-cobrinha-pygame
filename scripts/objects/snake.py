from random import randint


class Snake():
	def __init__(self, grid_size, unit_size):
		grid_units = (int(grid_size[0] / unit_size), int(grid_size[1] / unit_size))

		self.lives = 2
		self.size = 1
		front = randint(0, 3)
		self.direction = [front, 0]

		if front < 2:
			self.direction[1] = self.direction[0] + 2
		else:
			self.direction[1] = self.direction[0] - 2

		self.head = [
			self.direction,
			[
				randint(2, grid_units[0] - 3),
				randint(2, grid_units[1] - 3)
			]
		]
		self.segments = [self.head]
		self.addSegment()
		self.addSegment()


	def update(self):
		# Update nexts segments
		# for i in range(1, len(self.segments)):
		# 	self.segments[i] = self.segments[i - 1]

		x = y = 0

		# Update head
		if self.segments[0][0][1] == 0:
			x = -1
		elif self.segments[0][0][1] == 2:
			x = 1
		elif self.segments[0][0][1] == 1:
			y = -1
		else:
			y = 1
		
		self.segments[0][1][0] += x
		self.segments[0][1][1] += y




		## The following segments
		#for i in range(1, len(self.segments)):
		#	self.segments[i] = self.segments[i - 1]


	def setDirection(self):
		self.direction = [0, 0]


	def addSegment(self):
		self.size += 1
		x = y = 0

		if self.segments[-1][0][0] == 0:
			x = 1
		elif self.segments[-1][0][0] == 2:
			x = -1
		elif self.segments[-1][0][0] == 1:
			y = 1
		else:
			y = -1

		self.segments.append( [
			self.segments[-1][0],
			[
				self.segments[-1][1][0] + x,
				self.segments[-1][1][1] + y
			]
		] )
