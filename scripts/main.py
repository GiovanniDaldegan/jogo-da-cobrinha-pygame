import sys, os, pygame

import render, sceneManager
from settings import SETTINGS
from scenes import game, menu


# Game setup
base_path = os.getcwd()
source_path = os.path.join(base_path, "\\source")
pygame.init()

SCREEN = pygame.display.set_mode(SETTINGS["SCREEN_SIZE"])
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

## Layers: [scene setup, snake, layer2, layer3, ...]
layers = [[], []]


def main():
	run = True


	while run:

		events = pygame.event.get()

		for event in events:
			if event.type == pygame.QUIT: run = False

		sceneManager.runState(base_path, events, layers)

		render.renderScene(SCREEN, layers)
		# game.gameLoop(base_path, events, layers)

		clock.tick(SETTINGS["FPS"])

	pygame.quit()
	sys.exit()


if __name__ == "__main__": main()
