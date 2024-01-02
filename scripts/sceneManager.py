import interfaceHandler, loadManager

from settings import SETTINGS
from scenes.scn_menu import MenuScene
from scenes.scn_game import GameScene
from scenes.scn_settings import SettingsScene
from scenes.scn_store import StoreScene
from scenes.scn_test import Test


class SceneManager():
	"""
	Administra as cenas do jogo. Responsável por
	alternar as cenas, chamar as funções de cada
	cena e também a função de checagem de eventos
	relacionados aos elementos de UI.
    """

	def __init__(self):
		self.scenes = ["menu", "settings", "store", "game", "test"]
		self.current_state = None

		self.run = True

		# Load fonts
		self.fonts = loadManager.loadFonts(
			[
				["Pixeltype.ttf", SETTINGS["TEXT_SIZES"][0]],
				["Pixeltype.ttf", SETTINGS["TEXT_SIZES"][1]],
				["Pixeltype.ttf", SETTINGS["TEXT_SIZES"][2]],
				["Pixeltype.ttf", SETTINGS["TEXT_SIZES"][3]]
			]
		)


	def runState(self, events, layers):
		"""
		Chama a função da cena atual.

		Argumentos:
		---
		- events: eventos do pygame;
		- layers: camadas de renderização.
		"""

		# TODO: limpar esses argumentos.
		
		if not self.current_state:
			self.setScene(layers, 0)

		elif self.current_state == self.scenes[0]:
			self.menu_scene.menuLoop(events, layers, self)

		elif self.current_state == self.scenes[3]:
			self.game_scene.gameLoop(events, layers)
		
		elif self.current_state == self.scenes[4]:
			self.test_scene.testLoop(events, layers, self)

		interfaceHandler.handleInterface(events, self, layers)


	def setScene(self, layers, scene_index):
		"""
		Instancia a cena desejada e a torna a cena atual.

		Argumentos:
		---
		- scene_index: índice da cena de destino.
		"""

		if scene_index == -1:
			self.run = False
			return

		self.clearScreen(layers)
		self.current_state = self.scenes[scene_index]

		if self.current_state == self.scenes[0]:
			self.menu_scene = MenuScene(layers, self.fonts)

		elif self.current_state == self.scenes[1]:
			self.settings_scene = SettingsScene(layers, self.fonts)

		elif self.current_state == self.scenes[2]:
			self.store_scene = StoreScene(layers, self.fonts)

		elif self.current_state == self.scenes[3]:
			self.game_scene = GameScene(layers, self.fonts)

		elif self.current_state == self.scenes[4]:
			self.test_scene = Test(layers, self.fonts)


	def clearScreen(self, layers):
		"""
		Limpa todas as camadas de renderização.
		"""


		layers.clear()
		layers.append([])
		layers.append([])

	#TODO: transições
