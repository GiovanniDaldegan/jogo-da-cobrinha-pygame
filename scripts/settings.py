import sys
from os import path
from pygame import Vector2, color


# TODO: carregar e salvar configurações em arquivos

SETTINGS = {
	"FPS": 60,
	"SCREEN_SIZE": Vector2(1000, 700),
	"GRID_ORIGIN": Vector2(50, 200),
	"GRID_SIZE": Vector2(900, 450),
	"UNIT_SIZE": 50,
	"TEXT_SIZES": (200, 100, 60, 40)
}

# NOTE: checar se esse método funciona para obter o diretório com o programa compilado
if getattr(sys, 'frozen', False):
    SETTINGS["PARENT_DIR"] = path.dirname(sys.executable)
elif __file__:
    SETTINGS["PARENT_DIR"] = path.dirname(path.dirname(__file__))

SETTINGS["SCRIPTS_DIR"] = path.join(SETTINGS["PARENT_DIR"], "scripts")
SETTINGS["SOURCE_DIR"] = path.join(SETTINGS["PARENT_DIR"], "source")



COLORS = {
	"light_gray"	: color.Color(225, 225, 225),
	"purple"		: color.Color(230, 150, 230),
	"yellow"		: color.Color(255, 255, 0),
	"pink"			: color.Color(255, 0, 255),
    "red"			: color.Color(255, 50, 50)
}
