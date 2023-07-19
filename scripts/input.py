import pygame

def handeInput(event, player):
		
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_SPACE:
			player.addSegment()

	# if event.type == pygame.MOUSEBUTTONDOWN:
	# 	if rect.collidepoint(event.pos):
	# 		return True
		
