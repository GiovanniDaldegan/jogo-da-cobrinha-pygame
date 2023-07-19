from random import randint

def oneWayOrAnother():
	return [1, -1][randint(0, 1)]


class Snake():
	def __init__(self, grid_size, unit_size):
		grid_units = (int(grid_size[0] / unit_size), int(grid_size[1] / unit_size))

		self.size = 2
		self.direction = [0, 0, 0, 0]
		randIndex = randint(0, 3)

		if randIndex <= 1:
			self.direction[randIndex] = oneWayOrAnother()
			self.direction[randIndex + 2] = - self.direction[randIndex]
		elif randIndex >= 2:
			self.direction[randIndex] = oneWayOrAnother()
			self.direction[randIndex - 2] = - self.direction[randIndex]

		self.head = [
			self.direction,
			[
				randint(2, grid_units[0] - 2),
				randint(2, grid_units[1] - 2)
			]
		]
		self.segments = [self.head]
		self.addSegment()

		print(self.segments, end="\n\n")


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

