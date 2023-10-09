import loadManager
from objects import geometry, text, button, toggle, slider
from settings import SETTINGS, COLORS


class SettingsScene():
	def __init__(self, source_path, layers, fonts):
		sprites = {
			"toggle": loadManager.loadSpriteSheet(source_path, "toggle.png", 30, (1, 2)),
			"slider": [
				loadManager.loadSprite(source_path, "slider_background.png", color_key=(), additional_path="slider"),
				loadManager.loadSprite(source_path, "slider_fill.png", color_key=(), additional_path="slider"),
				loadManager.loadSprite(source_path, "slider_handle.png", color_key=(), additional_path="slider")
			]
		}

		# Scene objects
		title = text.Text( [
			{ "font": fonts[1], "content": "Configs", "pos": (500, 100), "color": COLORS["light_gray"] }
		] )

		volume_text = text.Text( [
			{ "font": fonts[2], "content": "Volume", "pos": (250, 300), "color": COLORS["light_gray"] }
		] )


		toggle_mute = toggle.Toggle((230, 365), False, sprites["toggle"], "")

		volume_slider = slider.Slider((600, 300), sprites["slider"], "set volume")

		back_button = button.Button(
			(70, 50),
			text.Text(
				[ { "font": fonts[3], "content": "Voltar", "pos": (0, -1), "color": COLORS["light_gray"] } ],
			), geometry.Rectangle(COLORS["light_gray"], (0, 0), (90, 40), 3), "switch 0"
		)

		# TODO: slider

		# volume_value = text.Text( [
		# 	{ "font": fonts["font3"], "content": "Configs", "pos": (504, 104), "color": COLORS["light_gray"] }
		# ] )

		theme_text = text.Text( [
			{ "font": fonts[2], "content": "Tema", "pos": (254, 404), "color": COLORS["light_gray"] }
		] )

		layers[0].append(title)
		layers[0].append(volume_text)
		layers[0].append(theme_text)

		layers[1].append(toggle_mute)
		layers[1].append(volume_slider)
		layers[1].append(back_button)
