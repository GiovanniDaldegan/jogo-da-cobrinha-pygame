import interface, loadManager, os

from settings import SETTINGS
from objects import geometry
from scenes.scn_menu import MenuScene
from scenes.scn_game import GameScene
from scenes.scn_settings import SettingsScene
from scenes.scn_store import StoreScene
from scenes.scn_test import Test


class SceneManager():
	def __init__(self, source_path):
		self.scenes = ["menu", "settings", "store", "game", "test"]
		self.current_state = None

		self.run = True

		# Load fonts
		self.fonts = loadManager.loadFonts(os.path.join(source_path, "source"),
			[
				["Pixeltype.ttf", SETTINGS["TEXT_SIZES"][0]],
				["Pixeltype.ttf", SETTINGS["TEXT_SIZES"][1]],
				["Pixeltype.ttf", SETTINGS["TEXT_SIZES"][2]],
				["Pixeltype.ttf", SETTINGS["TEXT_SIZES"][3]]
			]
		)


	def runState(self, source_path, events, layers):
		if not self.current_state:
			self.setScene(source_path, layers, 0)

		if self.current_state == self.scenes[0]:
			self.menu_scene.menuLoop(source_path, events, layers, self)

		elif self.current_state == self.scenes[3]:
			self.game_scene.gameLoop(source_path, events, layers)
		
		elif self.current_state == self.scenes[4]:
			self.test_scene.testLoop(source_path, events, layers, self)

		interface.handleInterface(events, source_path, self, layers)


	def setScene(self, source_path, layers, state_index):
		if state_index == -1:
			self.run = False
			return
		
		self.clearScreen(layers)
		self.current_state = self.scenes[state_index]

		if self.current_state == self.scenes[0]:
			self.menu_scene = MenuScene(source_path, layers, self.fonts)

		elif self.current_state == self.scenes[1]:
			self.settings_scene = SettingsScene(source_path, layers, self.fonts)

		elif self.current_state == self.scenes[2]:
			self.store_scene = StoreScene(source_path, layers, self.fonts)

		elif self.current_state == self.scenes[3]:
			self.game_scene = GameScene(source_path, layers, self.fonts)

		elif self.current_state == self.scenes[4]:
			self.test_scene = Test(source_path, layers, self.fonts)


	def clearScreen(self, layers):
		layers.clear()
		layers.append([])
		layers.append([])

	#TODO: transições
