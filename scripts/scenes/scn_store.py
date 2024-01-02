from pygame import Vector2

from settings import SETTINGS, COLORS
import loadManager

from objects import geometry, text
from objects.interfaceElements import Button


class StoreScene():
	"""
	Loja de itens.

    Argumentos:
    ---
	- layers: camadas de renderização do jogo;
	- fonts: fontes disponíveis.
    """

	def __init__(self, layers, fonts):
		# Scene objects
		title = text.Text( [
			{ "font": fonts[1], "content": "Loja", "pos": Vector2(500, 100), "color": COLORS["light_gray"] }
		] )

		back_button = Button(
			Vector2(70, 50),
			text.Text(
				[ { "font": fonts[3], "content": "Voltar", "pos": Vector2(0, -1), "color": COLORS["light_gray"] } ],
			), geometry.Rectangle(COLORS["light_gray"], (0, 0), (90, 40), 3), "switch 0"
		)

		layers[0].append(title)
		layers[1].append(back_button)
