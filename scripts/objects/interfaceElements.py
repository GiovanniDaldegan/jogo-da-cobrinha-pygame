"""

"""

from pygame import Vector2, Rect


class Toggle():
	"""
	Botão com valor binário.

    Argumentos:
    ---
	- pos: posição em pixels;
	- active: valor do botão;
	- sprites: sprites;
	- function: funcionalidade.
    """

	def __init__(self, pos:Vector2, active:bool, sprites, function:str):
		self.active = active
		self.rect = sprites[0].get_rect()
		self.rect.center = pos

		self.sprites = {
			"false": sprites[0],
			"true": sprites[1]
		}

		self.function = function


class Button():
	"""	
	Argumentos:
	---
	- pos: posição central;
	- rectangle: retângulo das bordas;
	- function: código de funcionalidade;
	- text: objeto de texto contido no botão.
	"""

	# TODO: sprites

	def __init__(self, pos:Vector2, text, rectangle:Rect, function:str):
		rectangle.rect.center = pos

		self.text = text
		self.rectangle = rectangle
		for i in range(len(self.text.rects)):
			self.text.rects[i].center = (self.text.rects[i].center[0] + pos.x, self.text.rects[i].center[1] + pos.y)

		self.function = function


class Slider():
	"""
	Controle deslizante.

    Argumentos:
    ---
	- pos: posição
	- sprites: respectivas sprites;
	- function: funcionalidade;
	- default_value: valor padrão.
    """

	def __init__(self, pos:Vector2, sprites, function:str, default_value:int=100):
		self.pos = pos
		self.value = default_value
		self.active = False
		self.function = function

		self.sprites = {
			"background": {
				"surface": sprites[0],
				"rect": sprites[0].get_rect(center=pos)
			},
			"fill": {
				"surface": sprites[1],
				"rect": sprites[1].get_rect(center=pos)
			},
			"handle": {
				"surface": sprites[2],
				"rect": sprites[2].get_rect(center=pos)
			}
		}

		self.setValue(self.value)

	def setValue(self, new_value):
		"""
		Atribui um novo valor ao slider.
		"""

		self.sprites["handle"]["rect"].center = (
			self.sprites["fill"]["rect"].left + new_value * (self.sprites["fill"]["rect"].size[0] / 100),
			self.sprites["handle"]["rect"].center[1]
		)


class ButtonList():
    def __init__(self, pos:Vector2, buttons, orientation:int, dist:int):
        """
        Agrupamento de botões.

        Argumentos:
        ---
        - pos: posição central.
        - buttons: botões para agrupar.
        - orientation: direção na qual o grupo está disposto indicates in which direction the list propagates.
          - 0 - horizontal
          - 1 - vertical
        - dist: distância entre cada botão.
        """

        self.pos = pos
        self.size = [0, 0]
        self.buttons = buttons
        self.buttons_pos = []

        self.size[orientation] = (len(buttons) - 1) * dist

        for i in range(len(buttons)):
            self.size[orientation] += buttons[i].rectangle.rect.size[orientation]

        self.size[orientation - 1] = buttons[0].rectangle.rect.size[orientation - 1]

        next_pos = [0, 0]
        next_pos[orientation] = self.pos[orientation] - self.size[orientation] / 2

        for i in range(len(buttons)):
            next_pos[orientation] += buttons[i].rectangle.rect.size[orientation] / 2

            if i != 0:
                next_pos[orientation] += dist

            # self.buttons_pos.append(next_pos)

            self.buttons[i].pos = next_pos
            self.buttons[i].rectangle.rect.center = (
                self.buttons[i].rectangle.rect.center[0] + self.pos[0],
                self.buttons[i].rectangle.rect.center[1] + self.pos[1],
            )

            for j in self.buttons[i].text.lines:
                j["pos"][0] += self.pos[0]
                j["pos"][1] += self.pos[1]
