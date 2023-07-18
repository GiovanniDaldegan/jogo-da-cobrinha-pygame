import pygame
from settings import SETTINGS

def initializeFonts():
	font0 = pygame.font.Font("C:/Users/Daldegan/Giovanni/Github/jogo-da-cobrinha-pygame/source/fonts/Pixeltype.ttf", SETTINGS["TEXT_SIZES"][0])
	font1 = pygame.font.Font("C:/Users/Daldegan/Giovanni/Github/jogo-da-cobrinha-pygame/source/fonts/Pixeltype.ttf", SETTINGS["TEXT_SIZES"][1])

	return {"font0": font0, "font1": font1}
