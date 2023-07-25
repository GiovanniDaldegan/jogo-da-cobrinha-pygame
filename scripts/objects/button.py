import pygame
from .geometry import Rectangle


class Button():
	def __init__(self, pos, text, rectangle, function):
		rectangle.rect.center = pos

		self.text = text
		self.rectangle = rectangle
		for i in range(len(self.text.rects)):
			self.text.rects[i].center = (self.text.rects[i].center[0] + pos[0], self.text.rects[i].center[1] + pos[1])

		self.function = function

# button "function" code
# [0]: what the button should do
#		("switch", "settings")
# [1]: first value
#		(scene index, which configuration to change)
# [2]: second value
#		(transition index, new configuration value)
