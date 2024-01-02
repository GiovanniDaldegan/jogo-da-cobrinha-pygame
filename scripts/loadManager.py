import os
from pygame import image, font, Surface, color

from settings import SETTINGS

def loadSpriteSheet(file_name:str, unit_size, tiles:list[int]=[1, 1], color_key:color.Color=(255, 255, 255, 255), folder_name=""):
	"""
	Carrega sprites diferentes de um mesmo arquivo.
	Todas são quadradas e têm o mesmo comprimento.

    Argumentos:
    ---
	- flie_name: nome do arquivo;
	- tiles: nº de linhas e nº de colunas, respect.;
	- color_key: cor do fundo;
	- folder_name: nome da pasta do arquivo.
    """

	original = image.load(os.path.join(SETTINGS["SOURCE_DIR"], "graphics", folder_name, file_name)).convert()
	sprites = []
	sprite_index = 0

	for i in range(tiles[0]):
		for j in range(tiles[1]):
			sprites.append(Surface((unit_size, unit_size)))
			sprites[sprite_index].blit(original, (0, 0), (j * unit_size, i * unit_size, unit_size, unit_size))
			sprites[sprite_index].set_colorkey(color_key)
			sprites[sprite_index].convert()
			sprite_index += 1

	return sprites

def loadSprite(file_name, color_key:color.Color=(255, 255, 255, 255), folder_name=""):
	"""
	Carrega uma única sprite.

    Argumentos:
    ---
	- flie_name: nome do arquivo;
	- color_key: cor do fundo;
	- folder_name: nome da pasta do arquivo.
	"""

	surface = image.load(os.path.join(SETTINGS["SOURCE_DIR"], "graphics", folder_name, file_name)).convert()
	if color_key != ():
		surface.set_colorkey(color_key)
	return surface

def loadFonts(requests):
	"""
	Carrega as fontes requeridas.

    Argumentos:
    ---
	- *requests: fontes a carregar.
    """

	fonts = []

	for i in requests:
		fonts.append(font.Font(os.path.join(SETTINGS["SOURCE_DIR"], "fonts", i[0]), i[1]))

	return fonts

# def loadFont(font_name, ):