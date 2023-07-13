# INCOMPLETO

class Polygon():
	def __init__(self, vertices, color, pos=(0,0)):
		super().__init__()

		for v in range(vertices):
			self[f"v{v}"] = vertices[v]
		self.color = color
