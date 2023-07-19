import pygame


def render_scene(SCREEN, layers):
	SCREEN.fill("#000000")

	# for j in range()

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

			elif obj_class == "Circle":
				pygame.draw.circle(SCREEN, obj.color, obj.pos, obj.radius)

			#elif obj_class == "Snake":


	pygame.display.update()
