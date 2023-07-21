from random import randint

def oneWayOrAnother():
	return [1, -1][randint(0, 1)]


class Snake():
	def __init__(self, grid_size, unit_size):
		grid_units = (int(grid_size[0] / unit_size), int(grid_size[1] / unit_size))

		self.size = 3
		self.direction = [0, 0, 0, 0]
		rand_index = randint(0, 3)

		if rand_index <= 1:
			self.direction[rand_index] = oneWayOrAnother()
			self.direction[rand_index + 2] = - self.direction[rand_index]
		elif rand_index >= 2:
			self.direction[rand_index] = oneWayOrAnother()
			self.direction[rand_index - 2] = - self.direction[rand_index]

		self.head = [
			self.direction,
			[
				randint(2, grid_units[0] - 2),
				randint(2, grid_units[1] - 2)
			]
		]
		self.segments = [self.head]
		self.addSegment()

		# print(self.segments, end="\n\n")


	def update(self):
		
		# Update position
		for i in range(len(self.segments) - 1, 1, -1):
			self.segments[i] = self.segments[i - 1]

		## Head
		direction = self.segments[0][0].index(1)
		if direction == 0:
			self.segments[0][1][0] += 1
		elif direction == 1:
			self.segments[0][1][1] += 1
		elif direction == 2:
			self.segments[0][1][0] -= 1
		else:
			self.segments[0][1][1] -= 1


	def setDirection(self):
		self.direction = [0, 0, 0, 0]


	def addSegment(self):
		self.size += 1
		self.segments.append([
			self.segments[-1][0], [self.segments[-1][1][0] - self.segments[-1][0][0], self.segments[-1][1][0] - self.segments[-1][0][1]]
		])

