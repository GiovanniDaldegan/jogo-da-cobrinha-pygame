import pygame, loadManager
from settings import SETTINGS, COLORS
from interface import handleInterface
from inputHandler import handleInput
from objects import geometry, text, button, grid, snake


class GameScene():
	def __init__(self, source_path, layers):
		layers.append([]) # layers[2] | snake
		layers.append([]) # layers[#] | etc

		# Fonts
		_fonts = loadManager.loadFonts(source_path,
			["Pixeltype.ttf", "Pixeltype.ttf", "Pixeltype.ttf"],
			[SETTINGS["TEXT_SIZES"][1], SETTINGS["TEXT_SIZES"][2], SETTINGS["TEXT_SIZES"][3]]
		)

		# Sprites
		self.sprites = {
			"snake": loadManager.loadSpriteSheet(source_path, "snake.png", 50, (2, 2))
		}

		# Time track & game speed
		self.game_speed = 1

		self.acceleration_timer = pygame.USEREVENT + 1
		pygame.time.set_timer(self.acceleration_timer, 8000)

		self.first_frame = pygame.time.get_ticks()
		self.last_frame = self.first_frame

		# General grid variables
		grid_size = SETTINGS["GRID_SIZE"]
		unit_size = SETTINGS["UNIT_SIZE"]
		grid_origin = SETTINGS["GRID_ORIGIN"]

		# Title
		title = text.Text(
			(
				{ "font": _fonts[1], "content":"JOGO DA", "pos": (504, 50), "color": COLORS["light_gray"] },
				{ "font": _fonts[0], "content": "COBRINHA", "pos": (504, 100), "color": COLORS["light_gray"] }
			)
		)

		# Borders
		r0 = geometry.Rectangle(COLORS["light_gray"], (46, 196), (907, 457), 6)

		# TODO: make sure the grid is at least 3x3 when it's customizable
		# Grid
		grame_grid = grid.Grid(grid_origin, grid_size, unit_size, (COLORS["light_gray"], COLORS["light_gray"]), 1)

		# Interface
		back_button = button.Button(
			(70, 50),
			text.Text(
				[ { "font": _fonts[2], "content": "Voltar", "pos": (2, 2), "color": COLORS["light_gray"] } ],
			), geometry.Rectangle(COLORS["light_gray"], (0, 0), (90, 40), 3), "switch 0"
		)

		# Game objects
		self.items = []

		self.snake = snake.Snake(grid_origin, grid_size, unit_size, self.sprites["snake"])
		self.setSnakeSprites()


		layers[0].append(title)
		layers[0].append(r0)
		layers[0].append(grame_grid)
		layers[1].append(back_button)
		layers[2].append(self.snake)


	def gameLoop(self, source_path, events, layers):
		_input = handleInput(events)

		this_tick = pygame.time.get_ticks()

		for event in events:
			if event.type == self.acceleration_timer:
				self.game_speed += 0.5

			# Input
			if event.type == pygame.KEYDOWN:

				# Snake movement
				new_direction = None
				if event.key == pygame.K_RIGHT:
					new_direction = [0, 2]
				elif event.key == pygame.K_DOWN:
					new_direction = [1, 3]
				elif event.key == pygame.K_LEFT:
					new_direction = [2, 0]
				elif event.key == pygame.K_UP:
					new_direction = [3, 1]
				
				if new_direction:
					self.snake.segments[0].direction = new_direction


		# Game slow fps update
		if ((this_tick - self.last_frame) * self.game_speed) / 1000 >= 1:
			self.last_frame = this_tick
			layers[2].clear()

			# Snake
			self.snake.update()
			layers[2].append(self.snake)

			self.setSnakeSprites()


		# Items
		# for i in range(len(self.items)):
		# 	layers[3].append(self.items[i].sprite)

		## Check items
		# for j in range(len(self.items)):
		# 	if self.items[j].pos == self.snake.segments[1][1]:
		# 		if type(self.items[j]).__name__ == "Apple":
		# 			self.items.pop(j)

		# 		if type(self.items[j]).__name__ == "Bomb":
		# 			self.items.pop(j)

		# NOTE: make a toggle and custom timer for bombs
		## Bomb timers


		# if self.snake.lives == 0: pygame.time.set_timer(self.acceleration_timer, 0)


	def setSnakeSprites(self):
		for i in range(len(self.snake.segments)):
			self.setSegmentRotation(i)

			if i == 0:
				self.snake.segments[0].sprite = "head"

			elif i == len(self.snake.segments) - 1:
				self.snake.segments[-1].sprite = "tail"

			else:
				self.snake.segments[i].sprite = "straight"
		

	def setSegmentRotation(self, i):
		direction_difference = abs(self.snake.segments[i].direction[0] - self.snake.segments[i].direction[1])
		direction_sum = self.snake.segments[i].direction[0] + self.snake.segments[i].direction[1]

		if direction_difference == 3:
			rotation = 1

		elif direction_difference == 2:
			rotation = range(0, 4)[- self.snake.segments[i].direction[0]]

		elif direction_difference == 1:
			if direction_sum == 1:
				rotation = 0
			if direction_sum == 3:
				rotation = 3
			if direction_sum == 5:
				rotation = 2

		self.snake.segments[i].rotation = rotation
