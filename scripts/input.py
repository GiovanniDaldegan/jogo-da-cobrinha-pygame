import pygame

def handeInput(events):

	for event in events:
		if event.type == pygame.KEYDOWN:
			return str(event.key)

		# if event.type == pygame.MOUSEBUTTONDOWN:
		# 	if rect.collidepoint(event.pos):
		# 		return True
		
