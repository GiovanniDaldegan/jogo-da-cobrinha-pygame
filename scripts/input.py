import pygame


def handleInput(events):

	for event in events:
		if event.type == pygame.KEYDOWN:
			return event.key
