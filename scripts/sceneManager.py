from scenes import menu, game


scenes = ["menu", "game"] # "Game over"?
current_scene = "menu"


def runState(base_path, events, layers):
	if current_scene == scenes[0]:
		menu.menuLoop(base_path, events, layers)
	elif current_scene == scenes[1]:
		game.setup(base_path, layers)
		game.gameLoop(base_path, events, layers)


def setState(layers, current_scene, new_state):
	layers = [[], []]
	current_scene = new_state
