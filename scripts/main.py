import sys, pygame

SETTINGS = {
	"FPS": 60,
	"SIZE": (1000, 700),
	"GRID_SIZE": 50,
	"TEXT_SIZES": (70, 45, 25)
	#"MAP_SIZE": (900, 0)
}

pygame.init()
WINDOW = pygame.display.set_mode(SETTINGS["SIZE"])
pygame.display.set_caption("Jogo da Cobrinha")

clock = pygame.time.Clock()

title_font = pygame.font.Font(None, SETTINGS["TEXT_SIZES"][0])


def draw_window(WINDOW):
	WINDOW.fill((0,0,0))

	title_surface0 = title_font.render("JOGO DA", False, (225, 225, 225))
	title_surface1 = title_font.render("COBRINHA", False, (225, 225, 225))

	WINDOW.blit(title_surface0, (390, 30))
	WINDOW.blit(title_surface1, (370, 70))

	pygame.draw.line(WINDOW, (255,255,255), (50, 200), (950, 200), 4)
	pygame.draw.line(WINDOW, (255,255,255), (950, 200), (950, 650), 4)
	pygame.draw.line(WINDOW, (255,255,255), (950, 650), (50, 650), 4)
	pygame.draw.line(WINDOW, (255,255,255), (50, 650), (50, 200), 4)

	pygame.display.update()


def main():
	run = True

	while run:

		events = pygame.event.get()

		for event in events:
			if event.type == pygame.QUIT: run = False

		draw_window(WINDOW)
		clock.tick(SETTINGS["FPS"])
	
	pygame.quit()
	sys.exit()

if __name__ == "__main__": main()
