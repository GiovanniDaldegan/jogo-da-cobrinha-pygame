import pygame
from settings import SETTINGS


def renderScene(SCREEN, layers):
	SCREEN.fill("#000000")

	# for j in range()

	for layer in layers:
		for obj in layer:
			obj_class = type(obj).__name__

			if obj_class == "Surface":
				SCREEN.blit(obj, (0, 0))
			
			elif obj_class == "Sprite":
				SCREEN.blit(obj.surface, obj.rect.topleft)

			elif obj_class == "Line":
				pygame.draw.line(SCREEN, obj.color, obj.start, obj.end, obj.width)

			elif obj_class == "Rectangle":
				pygame.draw.rect(SCREEN, obj.color, obj.rect, obj.width)

			elif obj_class == "Circle":
				pygame.draw.circle(SCREEN, obj.color, obj.pos, obj.radius)

			elif obj_class == "Grid":
				for i in obj.lines:
					pygame.draw.line(SCREEN, i.color, i.start, i.end, i.width)

			# UI
			elif obj_class == "Text":
				for i in range(len(obj.lines)):
					SCREEN.blit(obj.lines[i], obj.rects[i])

			elif obj_class == "Button":
				pygame.draw.rect(SCREEN, obj.rectangle.color, obj.rectangle.rect, obj.rectangle.width)

				for i in range(len(obj.text.lines)):
					SCREEN.blit(obj.text.lines[i], obj.text.rects[i])

			elif obj_class == "Toggle":
				if obj.active:
					SCREEN.blit(obj.sprites["true"], obj.rect)
				else:
					SCREEN.blit(obj.sprites["false"], obj.rect)

			elif obj_class == "Slider":
				for i in obj.sprites.values():
					SCREEN.blit(i["surface"], i["rect"])


			elif obj_class == "Snake":
				for i in obj.segments:
					SCREEN.blit(pygame.transform.rotate(obj.sprites[i.sprite], 90 * i.rotation),
		 				(
							SETTINGS["GRID_ORIGIN"][0] + i.pos[0] * SETTINGS["UNIT_SIZE"],
							SETTINGS["GRID_ORIGIN"][1] + i.pos[1] * SETTINGS["UNIT_SIZE"]
						))

	pygame.display.update()
