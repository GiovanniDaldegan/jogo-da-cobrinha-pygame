import pygame

class Rectangle():
	def __init__(self, color, topleft, size, width):

		self.color = color
		self.rect = pygame.Rect(topleft, size)
		self.width = width
