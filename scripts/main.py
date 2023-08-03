import sys, os, pygame

import render, sceneManager
from settings import SETTINGS


# Game setup
base_path = os.getcwd()
source_path = os.path.join(base_path, "source")
pygame.init()

SCREEN = pygame.display.set_mode(SETTINGS["SCREEN_SIZE"])
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

## Layers: [scene setup, interface, layer1, layer2, ...]
layers = []
current_state = None


def main():

	scene_manager = sceneManager.SceneManager()

	while scene_manager.run:

		events = pygame.event.get()

		for event in events:
			if event.type == pygame.QUIT:
				scene_manager.run = False

		scene_manager.runState(source_path, events, layers)

		render.renderScene(SCREEN, layers)

		clock.tick(SETTINGS["FPS"])

	pygame.quit()
	sys.exit()


if __name__ == "__main__": main()
