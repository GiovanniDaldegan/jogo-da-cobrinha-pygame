import pygame
from settings import SETTINGS, COLORS
from fonts import initializeFonts
from objects import geometry, text, button
from input import handleInput


class MenuScene():
	def __init__(self, base_path, layers):
		_fonts = initializeFonts(base_path)

		# Scene objects
		title = text.Text((
			{ "font": _fonts["font1"], "content": "JOGO DA", "pos": (504, 204), "color": COLORS["light_gray"] },
			{ "font": _fonts["font0"], "content": "COBRINHA", "pos": (504, 284), "color": COLORS["light_gray"] }
		))

		play_button = button.Button(
			(298, 500),
			text.Text(
				[ { "font": _fonts["font2"], "content": "Jogar", "pos": (2, 2), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (130, 55), 3), "switch 3"
		)

		config_button = button.Button(
			(458, 500),
			text.Text(
				[ { "font": _fonts["font2"], "content": "Configs", "pos": (2, 2), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (160, 55), 3), "switch 1"
		)

		store_button = button.Button(
			(603, 500),
			text.Text(
				[ { "font": _fonts["font2"], "content": "Loja", "pos": (2, 2), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (100, 55), 3), "switch 2"
		)

		exit_button = button.Button(
			(718, 500),
			text.Text(
				[ { "font": _fonts["font2"], "content": "Sair", "pos": (2, 2), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (100, 55), 3), "switch -1"
		)

		layers[0] = [title]
		layers[1] = [play_button, config_button, store_button, exit_button]


	def menuLoop(self, base_path, events, layers):
		_input = handleInput(events)
