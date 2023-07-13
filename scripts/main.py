import sys, pygame, json
import render
from objects import text, sprite, line, rectangle, polygon


SETTINGS = {
	"FPS": 60,
	"SIZE": (1000, 700),
	"GRID_SIZE": 50,
	"TEXT_SIZES": (100, 60, 40)
	#"MAP_SIZE": (900, 0)
}

COLORS = {
	"light-gray": (225,225,225),

}

pygame.init()

SCREEN = pygame.display.set_mode(SETTINGS["SIZE"])
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

# Fonts
small_title_font = pygame.font.Font("C:/Users/Daldegan/Giovanni/Github/jogo-da-cobrinha-pygame/source/fonts/Pixeltype.ttf", SETTINGS["TEXT_SIZES"][1])
title_font = pygame.font.Font("C:/Users/Daldegan/Giovanni/Github/jogo-da-cobrinha-pygame/source/fonts/Pixeltype.ttf", SETTINGS["TEXT_SIZES"][0])


title = text.Text(
	(
		{ "font": small_title_font, "content":"JOGO DA", "pos": (504, 50), "color": COLORS["light-gray"] },
		{ "font": title_font, "content": "COBRINHA", "pos": (504, 100), "color": COLORS["light-gray"] }
	)
)
snek = sprite.Sprite("C:/Users/Daldegan/Giovanni/Github/jogo-da-cobrinha-pygame/source/graphics/snake.png", (500, 350))
r0 = rectangle.Rectangle(COLORS["light-gray"], (50, 200), (900, 450), 5)


layers = [[r0, title, snek], []]

def draw_SCREEN(SCREEN):
	SCREEN.fill((0,0,0))

	# title_surface0 = small_title_font.render("JOGO DA", False, "White")
	# title_surface1 = title_font.render("COBRINHA", False, "White")

	# SCREEN.blit(title_surface0, (427, 30))
	# SCREEN.blit(title_surface1, (357, 70))

	pygame.draw.line(SCREEN, (255,255,255), (50, 200), (950, 200), 4)
	pygame.draw.line(SCREEN, (255,255,255), (950, 200), (950, 650), 4)
	pygame.draw.line(SCREEN, (255,255,255), (950, 650), (50, 650), 4)
	pygame.draw.line(SCREEN, (255,255,255), (50, 650), (50, 200), 4)

	pygame.display.update()


def main():
	run = True

	while run:

		events = pygame.event.get()

		for event in events:
			if event.type == pygame.QUIT: run = False

		# draw_SCREEN(SCREEN)
		render.render_scene(SCREEN, layers)

		clock.tick(SETTINGS["FPS"])
	
	pygame.quit()
	sys.exit()

if __name__ == "__main__": main()
