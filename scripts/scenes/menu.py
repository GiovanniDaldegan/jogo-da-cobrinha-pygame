import pygame
from settings import SETTINGS, COLORS
from fonts import initializeFonts
from objects import geometry, text, button
from input import handleInput

def setup(base_path, layers):
	# layers = [[]]
	print("PORRA")
	_fonts = initializeFonts(base_path)


	title0 = text.Text((
		{ "font": _fonts["font1"], "content": "JOGO DA", "pos": (504, 204), "color": COLORS["light_gray"] },
		{ "font": _fonts["font0"], "content": "COBRINHA", "pos": (504, 284), "color": COLORS["light_gray"] }
	))

	play_button = button.Button(
		text.Text( [
			{ "font": _fonts["font2"], "content": "Jogar", "pos": (2, 2), "color": COLORS["light_gray"] }
		] ), geometry.Rectangle(COLORS["light_gray"], (0, 0), (130, 55), 3), (298, 500)
	)

	config_button = button.Button(
		text.Text( [
			{ "font": _fonts["font2"], "content": "Configs", "pos": (2, 2), "color": COLORS["light_gray"] }
		] ), geometry.Rectangle(COLORS["light_gray"], (0, 0), (160, 55), 3), (458, 500)
	)

	store_button = button.Button(
		text.Text( [
			{ "font": _fonts["font2"], "content": "Loja", "pos": (2, 2), "color": COLORS["light_gray"] }
		] ), geometry.Rectangle(COLORS["light_gray"], (0, 0), (100, 55), 3), (603, 500)
	)

	exit_button = button.Button(
		text.Text( [
			{ "font": _fonts["font2"], "content": "Sair", "pos": (2, 2), "color": COLORS["light_gray"] }
		] ), geometry.Rectangle(COLORS["light_gray"], (0, 0), (100, 55), 3), (718, 500)
	)

	layers[0] = [title0, play_button, config_button, store_button, exit_button]


def menuLoop(base_path, events, layers):
	_input = handleInput(events)

	if _input == pygame.K_SPACE:
		return 1
