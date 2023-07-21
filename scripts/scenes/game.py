from settings import SETTINGS, COLORS
from objects import geometry, text, snake
from fonts import initializeFonts
from input import handleInput


def setup(source_path, layers):
	# layers = [[], []]
	print("CARALHO")

	_fonts = initializeFonts(source_path)

	# TODO: garantir que a grade tenha, pelo menos, dimensões 3x3
	# Grid
	grid_size = SETTINGS["GRID_SIZE"]
	unit_size = SETTINGS["UNIT_SIZE"]
	grid_origin = SETTINGS["GRID_ORIGIN"]

	# Title
	title = text.Text(
		(
			{ "font": _fonts["font2"], "content":"JOGO DA", "pos": (504, 50), "color": COLORS["light_gray"] },
			{ "font": _fonts["font1"], "content": "COBRINHA", "pos": (504, 100), "color": COLORS["light_gray"] }
		)
	)

	# Borders
	r0 = geometry.Rectangle(COLORS["light_gray"], (46, 196), (907, 457), 6)

	layers[0].append(title)
	layers[0].append(r0)

	for i in range(int(grid_size[0] / unit_size) - 1):
		layers[0].append(geometry.Line(COLORS["light_gray"], (grid_origin[0] + (1 + i) * unit_size, grid_origin[1]), (grid_origin[0] + (1 + i) * unit_size, grid_origin[1] + grid_size[1]), 1))

	for j in range(int(grid_size[1] / unit_size) - 1):
		layers[0].append(geometry.Line(COLORS["light_gray"], (grid_origin[0], grid_origin[1] + (1 + j) * unit_size), (grid_origin[0] + grid_size[0], grid_origin[1] + (1 + j) * unit_size), 1))


def gameLoop(base_path, events, layers):
	#layers[1] = []

	_input = handleInput(events)


	# player.update()
	"""
	print(f"\n[ {player.segments[0][0]}, ", end="")
	for i in range(len(player.segments)):

		print(f"{player.segments[i][1]}", end=" ]")

		layers[1].append(geometry.Circle(COLORS["pink"],
				(
					SETTINGS["GRID_ORIGIN"][0] + player.segments[i][1][0] * SETTINGS["UNIT_SIZE"],
					SETTINGS["GRID_ORIGIN"][1] + player.segments[i][1][1] * SETTINGS["UNIT_SIZE"]
				),
				4
			)
		)"""
