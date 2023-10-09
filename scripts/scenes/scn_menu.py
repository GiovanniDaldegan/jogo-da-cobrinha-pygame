import pygame, loadManager
from settings import SETTINGS, COLORS
from objects import geometry, text, button, buttonList
from inputHandler import handleInput


class MenuScene():
	def __init__(self, source_path, layers, fonts):

		# Scene objects
		title = text.Text((
			{ "font": fonts[1], "content": "JOGO DA", "pos": (500, 200), "color": COLORS["light_gray"] },
			{ "font": fonts[0], "content": "COBRINHA", "pos": (500, 290), "color": COLORS["light_gray"] }
		))

		play_button = button.Button(
			(300, 500),
			text.Text(
				[ { "font": fonts[2], "content": "Jogar", "pos": (0, -2), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (130, 50), 3), "switch 3"
		)

		config_button = button.Button(
			(460, 500),
			text.Text(
				[ { "font": fonts[2], "content": "Configs", "pos": (0, -2), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (160, 50), 3), "switch 1"
		)

		store_button = button.Button(
			(600, 500),
			text.Text(
				[ { "font": fonts[2], "content": "Loja", "pos": (0, -2), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (100, 50), 3), "switch 2"
		)

		exit_button = button.Button(
			(720, 500),
			text.Text(
				[ { "font": fonts[2], "content": "Sair", "pos": (0, 0), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (100, 50), 3), "switch -1"
		)

		layers[0] = [title]
		layers[1] = [play_button, config_button, store_button, exit_button]


	def menuLoop(self, source_path, events, layers, scene_manager):
		_input = handleInput(events)

		if pygame.K_ESCAPE in _input["KEYSDOWN"]:
			scene_manager.setScene(source_path, layers, 4)
