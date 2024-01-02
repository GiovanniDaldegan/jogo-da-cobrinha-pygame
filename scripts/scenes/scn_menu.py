from pygame import Vector2, K_ESCAPE

from settings import SETTINGS, COLORS
from inputHandler import handleInput

from objects import geometry, text
from objects.interfaceElements import Button



class MenuScene():
	"""
	Cena de menu. Mostra o título do jogo e permite
	o acesso de todas as demais cenas.

    Argumentos:
    ---
	- layers: camadas de renderização do jogo;
	- fonts: fontes disponíveis.
    """

	def __init__(self, layers, fonts):
		# Scene objects
		title = text.Text((
			{ "font": fonts[1], "content": "JOGO DA", "pos": Vector2(500, 200), "color": COLORS["light_gray"] },
			{ "font": fonts[0], "content": "COBRINHA", "pos": Vector2(500, 290), "color": COLORS["light_gray"] }
		))

		play_button = Button(
			Vector2(300, 500),
			text.Text(
				[ { "font": fonts[2], "content": "Jogar", "pos": Vector2(0, -2), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (130, 50), 3), "switch 3"
		)

		config_button = Button(
			Vector2(460, 500),
			text.Text(
				[ { "font": fonts[2], "content": "Configs", "pos": Vector2(0, -2), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (160, 50), 3), "switch 1"
		)

		store_button = Button(
			Vector2(600, 500),
			text.Text(
				[ { "font": fonts[2], "content": "Loja", "pos": Vector2(0, -2), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (100, 50), 3), "switch 2"
		)

		exit_button = Button(
			Vector2(720, 500),
			text.Text(
				[ { "font": fonts[2], "content": "Sair", "pos": Vector2(0, 0), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (100, 50), 3), "switch -1"
		)

		layers[0] = [title]
		layers[1] = [play_button, config_button, store_button, exit_button]


	def menuLoop(self, events, layers, scene_manager):
		_input = handleInput(events)

		if K_ESCAPE in _input["KEYSDOWN"]:
			scene_manager.setScene(layers, 4)
