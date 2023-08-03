import pygame


def handleInterface(events, base_path, scene_manager, layers):
	if not pygame.mouse.get_pressed()[0]: return

	mouse_pos = pygame.mouse.get_pos()

	for obj in layers[1]:
		obj_class = type(obj).__name__

		if obj_class == "Button":
			if obj.rectangle.rect.collidepoint(mouse_pos):
				function = obj.function.split()

				if function[0] == "switch":
					scene_manager.setScene(base_path, layers, int(function[1]))

		elif obj_class == "Toggle":
			if pygame.MOUSEBUTTONDOWN in [event.type for event in events] and obj.rect.collidepoint(mouse_pos):
				obj.active = not obj.active

				#function = obj.function.split()

		if obj_class == "Slider":
			if pygame.MOUSEBUTTONDOWN in [event.type for event in events] and obj.sprites["handle"]["rect"].collidepoint(mouse_pos):
				obj.active = True

			if obj.active:
				if pygame.MOUSEBUTTONUP in [event.type for event in events]:
					obj.active = False

				new_value = 100 * (mouse_pos[0] - obj.sprites["fill"]["rect"].left) / obj.sprites["fill"]["rect"].size[0]

				if new_value >= 0 and new_value <= 100:
					obj.setValue(new_value)
