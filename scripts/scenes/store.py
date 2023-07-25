from fonts import initializeFonts
from objects import geometry, text, button
from settings import SETTINGS, COLORS

class StoreScene():
	def __init__(self, base_path, layers):
		_fonts = initializeFonts(base_path)

		# Scene objects
		title = text.Text( [
			{ "font": _fonts["font1"], "content": "Loja", "pos": (504, 104), "color": COLORS["light_gray"] }
		] )

		layers[0].append(title)
