class Slider():
	def __init__(self, pos, sprites, function, default_value=100):
		self.pos = pos
		self.value = default_value
		self.active = False
		self.function = function

		self.sprites = {
			"background": {
				"surface": sprites[0],
				"rect": sprites[0].get_rect(center=pos)
			},
			"fill": {
				"surface": sprites[1],
				"rect": sprites[1].get_rect(center=pos)
			},
			"handle": {
				"surface": sprites[2],
				"rect": sprites[2].get_rect(center=pos)
			}
		}

		self.setValue(self.value)

	def setValue(self, new_value):
		self.sprites["handle"]["rect"].center = (
			self.sprites["fill"]["rect"].left + new_value * (self.sprites["fill"]["rect"].size[0] / 100),
			self.sprites["handle"]["rect"].center[1]
		)
