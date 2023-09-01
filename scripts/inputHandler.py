import pygame


def handleInput(events):

	_input = {
		"KEYSDOWN": [],
		"KEYSUP": [],
		"MOUSEBUTTONDOWN": [],
		"MOUSEBUTTONUP": []
	}

	for event in events:
		if event.type == pygame.KEYDOWN:
			_input["KEYSDOWN"].append(event.key)
		elif event.type == pygame.KEYUP:
			_input["KEYSUP"].append(event.key)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			_input["MOUSEBUTTONDOWN"].append(event.button)
		elif event.type == pygame.MOUSEBUTTONUP:
			_input["MOUSEBUTTONUP"].append(event.button)

	return _input
