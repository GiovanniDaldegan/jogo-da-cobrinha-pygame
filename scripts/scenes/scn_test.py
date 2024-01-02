from pygame import Vector2, K_ESCAPE

from settings import SETTINGS, COLORS
from inputHandler import handleInput

from objects import text, geometry
from objects.interfaceElements import Button, ButtonList

class Test():
	"""
	ISTO É UM TESTE.

    Argumentos:
    ---
	- layers: camadas de renderização do jogo;
	- fonts: fontes disponíveis.
    """

	def __init__(self, layers, fonts):

		mamaco3 = Button(
			Vector2(0, 0),
			text.Text(
				[ { "font": fonts[2], "content": "Mamaco", "pos": Vector2(0, 0), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (120, 50), 3),
			"samba 2 3"
		)

		mamaco1 = Button(
			Vector2(0, 0),
			text.Text(
				[ { "font": fonts[2], "content": "Mamaco", "pos": Vector2(0, 0), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (120, 50), 3),
			"samba 2 3"
		)

		mamaco2 = Button(
			Vector2(0, 0),
			text.Text(
				[ { "font": fonts[2], "content": "Mamaco", "pos": Vector2(0, 0), "color": COLORS["light_gray"] } ]
			),
			geometry.Rectangle(COLORS["light_gray"], (0, 0), (120, 50), 3),
			"samba 2 3"
		)

		button_menu = ButtonList(Vector2(500, 500), [mamaco1, mamaco2, mamaco3], 0, 10)

		self.fixed_objects = []#[button_menu]

		for i in self.fixed_objects: layers[0].append(i)


	def testLoop(self, events, layers, scene_manager):
		_input = handleInput(events)

		if K_ESCAPE in _input["KEYSDOWN"]:
			scene_manager.setScene(layers, 0)
