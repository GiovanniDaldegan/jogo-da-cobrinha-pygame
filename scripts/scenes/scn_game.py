from random import randint
from pygame import time, Vector2, USEREVENT

from settings import SETTINGS, COLORS
import loadManager
from inputHandler import handleInput

from objects import geometry, text, grid, snake, apple, bomb
from objects.interfaceElements import Button


class GameScene():
	"""
	Cena de jogo. Responsável pela integração do
	cenário com a cobrinha, os itens e as
	mecânicas de jogo.

    Argumentos:
    ---
	- layers: camadas de renderização do jogo;
	- fonts: fontes disponíveis.
    """

	def __init__(self, layers, fonts):
		layers.append([]) # layers[2] | snake
		layers.append([]) # layers[3] | items
		layers.append([]) # layers[4] | overlay

		# Sprites
		self.sprites = {
			"snake": loadManager.loadSpriteSheet("snake.png", 50, (2, 2)),
			"apple": loadManager.loadSprite("apple.png"),
			"bomb": loadManager.loadSprite("bomb.png"),
		}

		# Time track & game speed
		self.game_speed = 1

		self.acceleration_timer = USEREVENT + 1
		self.apple_timer = USEREVENT + 2
		self.bomb_timer = USEREVENT + 3

		time.set_timer(self.acceleration_timer, 8000)
		time.set_timer(self.apple_timer, 5000)
		time.set_timer(self.bomb_timer, 15000)

		self.first_frame = time.get_ticks()
		self.last_frame = self.first_frame

		# General grid variables
		grid_size = SETTINGS["GRID_SIZE"]
		unit_size = SETTINGS["UNIT_SIZE"]
		grid_origin = SETTINGS["GRID_ORIGIN"]

		# Title
		self.title = text.Text(
			(
				{ "font": fonts[2], "content":"JOGO DA", "pos": Vector2(500, 50), "color": COLORS["light_gray"] },
				{ "font": fonts[1], "content": "COBRINHA", "pos": Vector2(500, 100), "color": COLORS["light_gray"] }
			)
		)

		# Borders
		self.rect0 = geometry.Rectangle(COLORS["light_gray"], (46, 196), (907, 457), 6)

		# TODO: make sure the grid is at least 3x3 when it's customizable
		# Grid
		self.game_grid = grid.Grid(grid_origin, grid_size, Vector2(unit_size, unit_size), [COLORS["light_gray"], COLORS["light_gray"]], Vector2(1, 1))

		# Interface
		self.back_button = Button(
			Vector2(70, 50),
			text.Text(
				[ { "font": fonts[3], "content": "Voltar", "pos": Vector2(0, -1), "color": COLORS["light_gray"] } ],
			), geometry.Rectangle(COLORS["light_gray"], (0, 0), (90, 40), 3), "switch 0"
		)

		self.game_over_text = text.Text(
			[
				{ "font": fonts[0], "content": "GAME OVER", "pos": SETTINGS["SCREEN_SIZE"] / 2, "color": COLORS["red"] }
			]
		)

		# Game variables
		self.points = 0

		# Game objects
		self.items = []
		self.remove_items_i = []

		self.snake = snake.Snake(grid_size, unit_size, self.sprites["snake"])
		# self.setSnakeSprites()

		self.fixed_objects = [(self.title, 0), (self.rect0, 0), (self.game_grid, 0), (self.back_button, 1), (self.snake, 2)]

		for i in self.fixed_objects: layers[i[1]].append(i[0])


	def gameLoop(self, events, layers):
		slow_frame = False
		_input = handleInput(events)

		# Clear Layers
		for l in layers: l.clear()

		this_tick = time.get_ticks()

		if self.snake.lives != 0:
			for event in events:
				if event.type == self.acceleration_timer:
					self.game_speed += 0.5
				elif event.type == self.apple_timer:
					self.spawn_item("apple")
				elif event.type == self.bomb_timer:
					self.spawn_item("bomb")


			# Game slow fps update
			if ((this_tick - self.last_frame) * self.game_speed) / 1000 >= 1:
				self.last_frame = this_tick
				slow_frame = True

			self.snake.update(_input, slow_frame)


			# Items
			for i in range(len(self.items)):
				layers[3].append(self.items[i].sprite)

				if self.items[i].pos == self.snake.segments[0].pos:
					if type(self.items[i]).__name__ == "Apple":
						self.snake.addSegment()
						self.remove_items_i.append(i)
						self.points += 1

					if type(self.items[i]).__name__ == "Bomb":
						self.remove_items_i.append(i)
						self.snake.lives -= 1

			for i in range(len(self.remove_items_i)):
				self.items.pop(self.remove_items_i[i])

			self.remove_items_i.clear()
			# if self.snake.lives == 0: time.set_timer(self.acceleration_timer, 0)

		else:
			layers[3].append(self.game_over_text)
		
		for i in self.fixed_objects: layers[i[1]].append(i[0])


	def spawn_item(self, item):
		random_pos = self.getRandomPos()

		if item == "apple":
			self.items.append(apple.Apple(random_pos, self.sprites["apple"]))
		elif item == "bomb":
			self.items.append(bomb.Bomb(random_pos, self.sprites["bomb"]))


	def getRandomPos(self):
		grid_size = Vector2(
			SETTINGS["GRID_SIZE"].x / SETTINGS["UNIT_SIZE"],
			SETTINGS["GRID_SIZE"].y / SETTINGS["UNIT_SIZE"]
		)

		return Vector2(
			SETTINGS["GRID_ORIGIN"].x + randint(0, grid_size.x - 1) * SETTINGS["UNIT_SIZE"],
			SETTINGS["GRID_ORIGIN"].y + randint(0, grid_size.y - 1) * SETTINGS["UNIT_SIZE"]
		)
