import sys, os, pygame

import render, sceneManager
from settings import SETTINGS
# from scenes import game, menu


# Game setup
base_path = os.getcwd()
source_path = os.path.join(base_path, "\\source")
pygame.init()

SCREEN = pygame.display.set_mode(SETTINGS["SCREEN_SIZE"])
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

## Layers: [scene setup, snake, layer2, layer3, ...]
layers = [[], []]
current_state = None

def main():
	run = True

	scene_manager = sceneManager.SceneManager()


	while run:
		if not scene_manager.current_state:
			scene_manager.setState(base_path, layers, 0)


		events = pygame.event.get()

		for event in events:
			if event.type == pygame.QUIT:
				run = False

		scene_manager.runState(base_path, events, layers)

		render.renderScene(SCREEN, layers)

		clock.tick(SETTINGS["FPS"])

	pygame.quit()
	sys.exit()


if __name__ == "__main__": main()
