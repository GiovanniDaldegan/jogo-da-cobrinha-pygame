import pygame

def handleInput(events):

	for event in events:
		if event.type == pygame.KEYDOWN:
			return event.key

		# if event.type == pygame.MOUSEBUTTONDOWN:
		# 	if rect.collidepoint(event.pos):
		# 		return True
		
