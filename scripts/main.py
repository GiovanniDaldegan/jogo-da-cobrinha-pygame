import sys, pygame

import render, input
from settings import SETTINGS
from scenes import game, menu


# Game setup
base_path = sys.path[0]
pygame.init()

SCREEN = pygame.display.set_mode(SETTINGS["SCREEN_SIZE"])
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()


# Layers: [scene setup, layer0, layer1, ...]
layers = []


def main():
	run = True

	# TODO: scene manager
	game.setup(layers)

	while run:

		events = pygame.event.get()

		for event in events:
			if event.type == pygame.QUIT: run = False


		render.render_scene(SCREEN, layers)

		clock.tick(SETTINGS["FPS"])

	pygame.quit()
	sys.exit()

if __name__ == "__main__": main()
