import pygame

def handeInput(event, rect):
			
	# if event.type == pygame.KEYDOWN:
	# 	if event.key == pygame.K_RIGHT:


	if event.type == pygame.MOUSEBUTTONDOWN:
		if rect.collidepoint(event.pos):
			return True
		
