import pygame

class Sprite():
	def __init__(self, path, pos=(0,0)):
		super().__init__()

		self.surface = pygame.image.load(path).convert_alpha()
		self.rect = self.surface.get_rect(center = pos)
