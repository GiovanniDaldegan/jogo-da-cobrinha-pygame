import pygame

from settings import SETTINGS, COLORS
from inputHandler import handleInput
from objects import text, geometry, button, buttonList

class Test():
    def __init__(self, source_path, layers, fonts):

        mamaco3 = button.Button(
            (0, 0),
            text.Text(
                [ { "font": fonts[2], "content": "Mamaco", "pos": (0, 0), "color": COLORS["light_gray"] } ]
            ),
            geometry.Rectangle(COLORS["light_gray"], (0, 0), (120, 50), 3),
            "samba 2 3"
        )

        mamaco1 = button.Button(
            (0, 0),
            text.Text(
                [ { "font": fonts[2], "content": "Mamaco", "pos": (0, 0), "color": COLORS["light_gray"] } ]
            ),
            geometry.Rectangle(COLORS["light_gray"], (0, 0), (120, 50), 3),
            "samba 2 3"
        )

        mamaco2 = button.Button(
            (0, 0),
            text.Text(
                [ { "font": fonts[2], "content": "Mamaco", "pos": (0, 0), "color": COLORS["light_gray"] } ]
            ),
            geometry.Rectangle(COLORS["light_gray"], (0, 0), (120, 50), 3),
            "samba 2 3"
        )

        button_menu = buttonList.ButtonList((500, 500), [mamaco1, mamaco2, mamaco3], 0, 10)

        self.fixed_objects = [button_menu]

        for i in self.fixed_objects: layers[0].append(i)


    def testLoop(self, source_path, events, layers, scene_manager):
        _input = handleInput(events)

        if pygame.K_ESCAPE in _input["KEYSDOWN"]:
            scene_manager.setScene(source_path, layers, 0)
