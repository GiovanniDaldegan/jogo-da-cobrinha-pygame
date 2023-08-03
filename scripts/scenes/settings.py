import loadManager
from objects import geometry, text, button, toggle, slider
from settings import SETTINGS, COLORS


class SettingsScene():
	def __init__(self, source_path, layers):
		_fonts = loadManager.loadFonts(source_path,
			["Pixeltype.ttf", "Pixeltype.ttf", "Pixeltype.ttf"],
			[SETTINGS["TEXT_SIZES"][1], SETTINGS["TEXT_SIZES"][2], SETTINGS["TEXT_SIZES"][3]]
		)

		sprites = {
			"toggle": loadManager.loadSpriteSheet(source_path, "toggle.png", 30, (1, 2)),
			"slider": [
				loadManager.loadSprite(source_path, "slider_background.png", additional_path="slider"),
				loadManager.loadSprite(source_path, "slider_fill.png", additional_path="slider"),
				loadManager.loadSprite(source_path, "slider_handle.png", additional_path="slider")
			]
		}

		# Scene objects
		title = text.Text( [
			{ "font": _fonts[0], "content": "Configs", "pos": (504, 104), "color": COLORS["light_gray"] }
		] )

		volume_text = text.Text( [
			{ "font": _fonts[1], "content": "Volume", "pos": (254, 304), "color": COLORS["light_gray"] }
		] )


		toggle_mute = toggle.Toggle((230, 365), False, sprites["toggle"], "")

		volume_slider = slider.Slider((600, 300), sprites["slider"], "set volume")

		back_button = button.Button(
			(70, 50),
			text.Text(
				[ { "font": _fonts[2], "content": "Voltar", "pos": (2, 2), "color": COLORS["light_gray"] } ],
			), geometry.Rectangle(COLORS["light_gray"], (0, 0), (90, 40), 3), "switch 0"
		)

		# TODO: slider

		# volume_value = text.Text( [
		# 	{ "font": _fonts["font3"], "content": "Configs", "pos": (504, 104), "color": COLORS["light_gray"] }
		# ] )

		theme_text = text.Text( [
			{ "font": _fonts[1], "content": "Tema", "pos": (254, 404), "color": COLORS["light_gray"] }
		] )

		layers[0].append(title)
		layers[0].append(volume_text)
		layers[0].append(theme_text)

		layers[1].append(toggle_mute)
		layers[1].append(volume_slider)
		layers[1].append(back_button)
