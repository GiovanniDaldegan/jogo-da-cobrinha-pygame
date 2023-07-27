import pygame

def handleInterface(base_path, scene_manager, layers):
	if not pygame.mouse.get_pressed()[0]: return

	for obj in layers[1]:
		
		if type(obj).__name__ == "Button":
			if obj.rectangle.rect.collidepoint(pygame.mouse.get_pos()):
				function = obj.function.split()
				
				if function[0] == "switch":
					scene_manager.setScene(base_path, layers, int(function[1]))

# TODO: toggle, slider
