from scenes import menu, game

class SceneManager():
	def __init__(self):
		self.scenes = ["menu", "game"] # "Game over"?
		self.current_state = None


	def runState(self, base_path, events, layers):
		if self.current_state == "menu":
			state_index = menu.menuLoop(base_path, events, layers)

			if state_index != None:
				self.setState(base_path, layers, state_index)

		elif self.current_state == "game":
			state_index = game.gameLoop(base_path, events, layers)

			if state_index != None:
				self.setState(base_path, layers, state_index)


	def setState(self, source_path, layers, state_index):

		print(f"Última cena: {self.current_state}")
		# layers = [[], []]
		self.current_state = self.scenes[state_index]
		print(f"Próxima: {self.current_state}")

		if self.current_state == "menu":
			menu.setup(source_path, layers)

		elif self.current_state == "game":
			game.setup(source_path, layers)
