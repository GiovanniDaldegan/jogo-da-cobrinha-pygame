import loadManager
from objects import geometry, text, button
from settings import SETTINGS, COLORS

class StoreScene():
	def __init__(self, source_path, layers, fonts):
		# Scene objects
		title = text.Text( [
			{ "font": fonts[1], "content": "Loja", "pos": (500, 100), "color": COLORS["light_gray"] }
		] )

		back_button = button.Button(
			(70, 50),
			text.Text(
				[ { "font": fonts[3], "content": "Voltar", "pos": (0, -1), "color": COLORS["light_gray"] } ],
			), geometry.Rectangle(COLORS["light_gray"], (0, 0), (90, 40), 3), "switch 0"
		)

		layers[0].append(title)
		layers[1].append(back_button)
