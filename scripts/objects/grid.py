from objects import geometry


class Grid():
	def __init__(self, grid_origin, grid_size, unit_size, colors, width):
		self.lines = []

		for i in range(1, int(grid_size[0] / unit_size)):
			self.lines.append(geometry.Line(
				colors[1],
				(grid_origin[0] + i * unit_size, grid_origin[1]),
				(grid_origin[0] + i * unit_size, grid_origin[1] + grid_size[1]),
				width
			))

		for j in range(1, int(grid_size[1] / unit_size)):
			self.lines.append(geometry.Line(
				colors[0],
				(grid_origin[0], grid_origin[1] + j * unit_size),
				(grid_origin[0] + grid_size[0], grid_origin[1] + j * unit_size),
				width
			))

			# geometry.Line(
			# 	(grid_origin[0] + (1 + i) * unit_size, grid_origin[1]),
			# 	(grid_origin[0] + (1 + i) * unit_size, grid_origin[1] + grid_size[1]), 1)

			# geometry.Line(
			# 	(grid_origin[0], grid_origin[1] + (1 + j) * unit_size),
			# 	(grid_origin[0] + grid_size[0], grid_origin[1] + (1 + j) * unit_size), 1)
