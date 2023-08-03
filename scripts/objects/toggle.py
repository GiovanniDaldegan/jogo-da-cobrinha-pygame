class Toggle():
	def __init__(self, pos, active, sprites, function):
		self.active = active
		self.rect = sprites[0].get_rect()
		self.rect.center = pos

		self.sprites = {
			"false": sprites[0],
			"true": sprites[1]
		}

		self.function = function
