import pygame

class Line():
	def __init__(self, color, start, end, width):
		self.color = color
		self.start = start
		self.end = end
		self.width = width

class Rectangle():
	def __init__(self, color, topleft, size, width):
		self.color = color
		self.rect = pygame.Rect(topleft, size)
		self.width = width

class Circle():
	def __init__(self, color, pos, radius):
		self.color = color
		self.pos = pos
		self.radius = radius
		# self.width = width

# INCOMPLETO
class Polygon():
	def __init__(self, vertices, color, pos=(0,0)):
		super().__init__()

		for v in range(vertices):
			self[f"v{v}"] = vertices[v]
		self.color = color
