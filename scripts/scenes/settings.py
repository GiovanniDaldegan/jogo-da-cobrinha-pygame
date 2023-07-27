from fonts import initializeFonts
from objects import geometry, text, button
from settings import SETTINGS, COLORS

class SettingsScene():
	def __init__(self, base_path, layers):
		_fonts = initializeFonts(base_path)

		# Scene objects
		title = text.Text( [
			{ "font": _fonts["font1"], "content": "Configs", "pos": (504, 104), "color": COLORS["light_gray"] }
		] )

		volume_text = text.Text( [
			{ "font": _fonts["font2"], "content": "Volume", "pos": (254, 304), "color": COLORS["light_gray"] }
		] )

		back_button = button.Button(
			(70, 50),
			text.Text(
				[ { "font": _fonts["font3"], "content": "Voltar", "pos": (2, 2), "color": COLORS["light_gray"] } ],
			), geometry.Rectangle(COLORS["light_gray"], (0, 0), (90, 40), 3), "switch 0"
		)

		# TODO: slider

		# volume_value = text.Text( [
		# 	{ "font": _fonts["font3"], "content": "Configs", "pos": (504, 104), "color": COLORS["light_gray"] }
		# ] )

		theme_text = text.Text( [
			{ "font": _fonts["font2"], "content": "Tema", "pos": (254, 404), "color": COLORS["light_gray"] }
		] )

		layers[0].append(title)
		layers[0].append(volume_text)
		layers[0].append(theme_text)

		layers[1].append(back_button)
