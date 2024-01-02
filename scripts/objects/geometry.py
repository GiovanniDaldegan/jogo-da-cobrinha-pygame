from pygame import Vector2, Rect, color

class Line():
	"""
	Argumentos:
	---
	- color: cor;
	- start: vetor de início;
	- end: vetor de fim;
	- width: grossura.
	"""

	def __init__(self, _color:color.Color, start:Vector2, end:Vector2, width=2):
		self.color = color
		self.start = start
		self.end = end
		self.width = width

class Rectangle():
	"""
	Argumentos:
	---
	- color: cor;
	- topleft: coordenada superior esquerda;
	- size: vetor com largura e altura;
	- width: largura do traço.
	"""

	def __init__(self, _color:color.Color, topleft:Vector2, size:Vector2, width:float):
		self.color = _color
		self.rect = Rect(topleft, size)
		self.width = width

class Circle():
	"""
	Argumentos:
	---
	- color: cor;
	- pos: posição central em pixels;
	- radius: raio.
	"""

	def __init__(self, _color:color.Color, pos:Vector2, radius:float):
		self.color = color
		self.pos = pos
		self.radius = radius
		# self.width = width

# INCOMPLETO
class Polygon():
	"""
	Polígono arbtrário.

	Argumentos:
	---
	- color: cor;
	- vertices: vetores dos vértices do polígono;
	- pos: posição central do polítono em pixels.
	"""

	def __init__(self, _color:color.Color, vertices:list[Vector2], pos:Vector2):
		super().__init__()

		for v in range(vertices):
			self[f"v{v}"] = vertices[v]
		self.color = color
