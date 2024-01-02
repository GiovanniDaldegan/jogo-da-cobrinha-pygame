from pygame import Vector2, color

from settings import COLORS
from objects import geometry


class Grid():
	"""
	Grade customizável, formada por linhas
	
    Argumentos:
    ---
	- grid_origin: posição do canto superior direito;
	- grid_size: com largura e altura da grade;
	- unit_size: lagura e altura da célula;
	- colors: lista com a cor das linhas e colunas (respect.);
	- widths: largura das linhas e colunas (respect.).
    """
	
	def __init__(self, grid_origin:Vector2, grid_size:Vector2, unit_size:Vector2, colors:list[color.Color], widths:Vector2):
		self.lines = []

		for i in range(1, int(grid_size.x / unit_size.x)):
			self.lines.append(geometry.Line(
				colors[1],
				(grid_origin.x + i * unit_size.y, grid_origin.y),
				(grid_origin.x + i * unit_size.y, grid_origin.y + grid_size.y),
				int(widths[1])
			))

		for j in range(1, int(grid_size.y / unit_size.y)):
			self.lines.append(geometry.Line(
				colors[0],
				(grid_origin.x, grid_origin.y + j * unit_size.y),
				(grid_origin.x + grid_size.x, grid_origin.y + j * unit_size.y),
				int(widths[0])
			))

