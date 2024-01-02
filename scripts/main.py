import sys, pygame

import render, sceneManager
from settings import SETTINGS


# Pygame setup
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

		# TODO: descentralizar `events`
		scene_manager.runState(events, layers)

		render.renderScene(SCREEN, layers)

		clock.tick(SETTINGS["FPS"])

	pygame.quit()
	sys.exit()


if __name__ == "__main__": main()
