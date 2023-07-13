import pygame
# from ..scripts.main import SETTINGS


def render_scene(SCREEN, layers):
	SCREEN.fill("#000000")

	for layer in layers:
		for obj in layer:
			obj_class = type(obj).__name__

			if obj_class == "Sprite":
				SCREEN.blit(obj.surface, obj.rect.topleft)

			elif obj_class == "Line":
				pygame.draw.line(SCREEN, obj.color, obj.start, obj.end, obj.width)

			elif obj_class == "Rectangle":
				pygame.draw.rect(SCREEN, obj.color, obj.rect, obj.width)

			elif obj_class == "Text":
				for l in range(len(obj.lines)):
					SCREEN.blit(obj.lines[l], obj.rects[l])



	pygame.display.update()