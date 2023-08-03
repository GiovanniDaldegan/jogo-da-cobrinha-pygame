from scenes.menu import MenuScene
from scenes.game import GameScene
from scenes.settings import SettingsScene
from scenes.store import StoreScene

from objects import geometry
import interface


class SceneManager():
	def __init__(self):
		self.scenes = ["menu", "settings", "store", "game"]
		self.current_state = None

		self.run = True


	def runState(self, base_path, events, layers):
		if not self.current_state:
			self.setScene(base_path, layers, 0)


		if self.current_state == self.scenes[0]:
			self.menu_scene.menuLoop(base_path, events, layers)

		elif self.current_state == self.scenes[3]:
			self.game_scene.gameLoop(base_path, events, layers)
		
		interface.handleInterface(events, base_path, self, layers)

	def setScene(self, source_path, layers, state_index):
		if state_index == -1:
			self.run = False
		
		self.clearScreen(layers)
		self.current_state = self.scenes[state_index]

		if self.current_state == self.scenes[0]:
			self.menu_scene = MenuScene(source_path, layers)

		elif self.current_state == self.scenes[1]:
			self.settings_scene = SettingsScene(source_path, layers)

		elif self.current_state == self.scenes[2]:
			self.store_scene = StoreScene(source_path, layers)

		elif self.current_state == self.scenes[3]:
			self.game_scene = GameScene(source_path, layers)


	def clearScreen(self, layers):
		layers.clear()
		layers.append([])
		layers.append([])

	#TODO: transições
