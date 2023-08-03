import os, pygame


def loadSpriteSheet(source_path, file_name, unit_size, tiles=(1, 1), color_key=(255, 255, 255), additional_path=""):
	original = pygame.image.load(os.path.join(source_path, "graphics", additional_path, file_name)).convert()
	sprites = []
	sprite_index = 0

	for i in range(tiles[0]):
		for j in range(tiles[1]):
			sprites.append(pygame.Surface((unit_size, unit_size)))
			sprites[sprite_index].blit(original, (0, 0), (j * unit_size, i * unit_size, unit_size, unit_size))
			sprites[sprite_index].set_colorkey(color_key)
			sprites[sprite_index].convert()
			sprite_index += 1

	return sprites

def loadSprite(source_path, file_name, color_key=(255, 255, 255), additional_path=""):
	return pygame.image.load(os.path.join(source_path, "graphics", additional_path, file_name)).convert()

def loadFonts(source_path, font_names, sizes):
	fonts = []
	
	for i in range(len(font_names)):
		fonts.append(pygame.font.Font(os.path.join(source_path, "fonts", font_names[i]), sizes[i]))

	return fonts

# def loadFont(source_path, font_name, ):