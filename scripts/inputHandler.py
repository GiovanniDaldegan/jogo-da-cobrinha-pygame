from pygame import KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP


def handleInput(events):
	"""
	Função responsável pelo registro das entradas de
	interesse (mouse e teclado).

    Argumentos:
    ---
	- events: eventos do pygame.
    """


	_input = {
		"KEYSDOWN": [],
		"KEYSUP": [],
		"MOUSEBUTTONDOWN": [],
		"MOUSEBUTTONUP": []
	}

	for event in events:
		if event.type == KEYDOWN:
			_input["KEYSDOWN"].append(event.key)
		elif event.type == KEYUP:
			_input["KEYSUP"].append(event.key)
		elif event.type == MOUSEBUTTONDOWN:
			_input["MOUSEBUTTONDOWN"].append(event.button)
		elif event.type == MOUSEBUTTONUP:
			_input["MOUSEBUTTONUP"].append(event.button)

	return _input
