from settings import SETTINGS, COLORS
from objects import geometry, text
from fonts import initializeFonts

def setup(layers):
	_fonts = initializeFonts()

	# Grid
	grid_size = SETTINGS["GRID_SIZE"]
	unit_size = SETTINGS["UNIT_SIZE"]
	grid_origin = SETTINGS["GRID_ORIGIN"]

	# Title
	title = text.Text(
		(
			{ "font": _fonts["font1"], "content":"JOGO DA", "pos": (504, 50), "color": COLORS["light_gray"] },
			{ "font": _fonts["font0"], "content": "COBRINHA", "pos": (504, 100), "color": COLORS["light_gray"] }
		)
	)

	# Borders
	r0 = geometry.Rectangle(COLORS["light_gray"], (46, 196), (907, 457), 6)

	layers.append([title, r0])

	for i in range(int(grid_size[0] / unit_size) - 1):
		layers[0].append(geometry.Line(COLORS["light_gray"], (grid_origin[0] + (1 + i) * unit_size, grid_origin[1]), (grid_origin[0] + (1 + i) * unit_size, grid_origin[1] + grid_size[1]), 1))

	for j in range(int(grid_size[1] / unit_size) - 1):
		layers[0].append(geometry.Line(COLORS["light_gray"], (grid_origin[0], grid_origin[1] + (1 + j) * unit_size), (grid_origin[0] + grid_size[0], grid_origin[1] + (1 + j) * unit_size), 1))

