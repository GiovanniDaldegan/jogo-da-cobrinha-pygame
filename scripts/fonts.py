import os, pygame
from settings import SETTINGS

def initializeFonts(source_path):
	font0 = pygame.font.Font(os.path.join(source_path, "source\\fonts\\Pixeltype.ttf"), SETTINGS["TEXT_SIZES"][0])
	font1 = pygame.font.Font(os.path.join(source_path, "source\\fonts\\Pixeltype.ttf"), SETTINGS["TEXT_SIZES"][1])

	return {"font0": font0, "font1": font1}
