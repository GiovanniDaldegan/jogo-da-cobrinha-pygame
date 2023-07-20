from settings import SETTINGS, COLORS
from fonts import initializeFonts
from objects import geometry, text, button
from input import handeInput

def menuLoop(base_path, events, layers):
	_fonts = initializeFonts(base_path)

	# _input = handeInput()
	
	# if _input == "K_SPACE":


	title0 = text.Text((
		{ "font": _fonts["font1"], "content": "JOGO DA", "pos": (504, 204), "color": COLORS["light_gray"] },
		{ "font": _fonts["font0"], "content": "COBRINHA", "pos": (504, 284), "color": COLORS["light_gray"] }
	))

	play_button = button.Button(
		text.Text( [
			{ "font": _fonts["font2"], "content": "Jogar", "pos": (2, 2), "color": COLORS["light_gray"] }
			]
		), geometry.Rectangle(COLORS["light_gray"], (0, 0), (130, 55), 3), (500, 500)
	)


	layers[0].append(title0)
	layers[0].append(play_button)
