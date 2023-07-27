import pygame
from settings import SETTINGS, COLORS
from interface import handleInterface
from input import handleInput
from fonts import initializeFonts
from objects import geometry, text, snake, button, grid


class GameScene():
	def __init__(self, source_path, layers):
		layers.append([]) # layers[2] | snake
		layers.append([]) # layers[#] | etc

		_fonts = initializeFonts(source_path)

		# Time track & game speed
		self.game_speed = 1

		self.acceleration_timer = pygame.USEREVENT + 1
		pygame.time.set_timer(self.acceleration_timer, 10000)

		self.first_frame = pygame.time.get_ticks()
		self.last_frame = self.first_frame

		# General grid variables
		grid_size = SETTINGS["GRID_SIZE"]
		unit_size = SETTINGS["UNIT_SIZE"]
		grid_origin = SETTINGS["GRID_ORIGIN"]

		# Title
		title = text.Text(
			(
				{ "font": _fonts["font2"], "content":"JOGO DA", "pos": (504, 50), "color": COLORS["light_gray"] },
				{ "font": _fonts["font1"], "content": "COBRINHA", "pos": (504, 100), "color": COLORS["light_gray"] }
			)
		)

		# Borders
		r0 = geometry.Rectangle(COLORS["light_gray"], (46, 196), (907, 457), 6)

		# TODO: make sure the grid is at least 3x3
		# Grid
		grame_grid = grid.Grid(grid_origin, grid_size, unit_size, (COLORS["light_gray"], COLORS["light_gray"]), 1)

		# Interface
		back_button = button.Button(
			(70, 50),
			text.Text(
				[ { "font": _fonts["font3"], "content": "Voltar", "pos": (2, 2), "color": COLORS["light_gray"] } ],
			), geometry.Rectangle(COLORS["light_gray"], (0, 0), (90, 40), 3), "switch 0"
		)

		# Game objects
		self.items = []

		self.snake = snake.Snake(grid_size, unit_size)


		layers[0].append(title)
		layers[0].append(r0)
		layers[0].append(grame_grid)
		layers[1].append(back_button)


	def gameLoop(self, base_path, events, layers):

		_input = handleInput(events)

		this_tick = pygame.time.get_ticks()

		for event in events:
			if event.type == self.acceleration_timer:
				self.game_speed += 0.5 #NOTE: speed speeds too fast
				print("AZERELA")

			if event.type == pygame.KEYDOWN:
				print(event.key, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP)

				if event.key == pygame.K_RIGHT:
					self.snake.direction = [0, 2]
				if event.key == pygame.K_DOWN:
					self.snake.direction = [1, 3]
				if event.key == pygame.K_LEFT:
					self.snake.direction = [2, 0]
				if event.key == pygame.K_UP:
					self.snake.direction = [3, 1]

		# Game slow fps update
		if ((this_tick - self.last_frame) * self.game_speed) / 1000 >= 1:
			self.last_frame = this_tick
			self.snake.update()

			for i in self.snake.segments:
				print(i[1],end=", ")

			layers[2].clear()


			print("\nsamba")

		# Snake
		for i in range(len(self.snake.segments)):
			layers[2].append(geometry.Circle(COLORS["pink"],
					(
						SETTINGS["GRID_ORIGIN"][0] + self.snake.segments[i][1][0] * SETTINGS["UNIT_SIZE"],
						SETTINGS["GRID_ORIGIN"][1] + self.snake.segments[i][1][1] * SETTINGS["UNIT_SIZE"]
					),
					4
				)
			)

		# for i in range(len(self.items)):
		# 	layers[3].append(self.items[i].sprite)

		# Check items
		# for j in range(len(self.items)):
		# 	if self.items[j].pos == self.snake.segments[1][1]:
		# 		if type(self.items[j]).__name__ == "Apple":
		# 			self.items.pop(j)

		# 		if type(self.items[j]).__name__ == "Bomb":
		# 			self.items.pop(j)

		# NOTE: make a toggle and custom timer for bombs
		# Bomb timers


		# if self.snake.lives == 0: pygame.time.set_timer(self.acceleration_timer, 0)


