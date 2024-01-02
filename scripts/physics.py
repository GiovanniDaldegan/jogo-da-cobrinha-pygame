class Vector2D():
	def __init__(self, x:int, y:int):
		"""
		Vetor bidimensional.
		"""

		self.x = x
		self.y = y


class Matrix():
	def __init__(self, vSize:int, *vectors: list | Vector2D):
		"""
		Matriz com vetores de tamanho `vSize`.

		Argumentos:
		---
		vSize: tamanho dos vetores nessa matriz.
		vectors: (opcional) vetores a inserir à matriz.
		"""

		self.vSize = vSize
		self.vectors = []

		for i in vectors:
			if i.__class__ == Vector2D:
				self.vectors.append([i.x, i.y])

			else:
				if len(i) != self.vSize:
					print(f"Matrix(): tentativa de adicionar vetor de tamanho {len(i)} em matriz de tamanho {self.vSize}.")
					return

				self.vectors.append(i)


	def add(self, *vectors: list | Vector2D):
		"""
		Argumentos:
		---
		vectors: vetores a inserir à matriz.
		"""
		for i in vectors:
			if i.__class__ == Vector2D:
				self.vectors.append([i.x, i.y])

			else:
				if len(i) != self.vSize:
					print(f"Matrix(): tentativa de adicionar vetor de tamanho {len(i)} em matriz de tamanho {self.vSize}.")
					return

				self.vectors.append(i)
