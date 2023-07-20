import pygame
from .geometry import Rectangle


class Button():
	def __init__(self, text, rectangle, pos):
		rectangle.rect.center = pos

		self.text = text
		self.rectangle = rectangle
		for i in range(len(self.text.rects)):
			self.text.rects[i].center = (self.text.rects[i].center[0] + pos[0], self.text.rects[i].center[1] + pos[1])
