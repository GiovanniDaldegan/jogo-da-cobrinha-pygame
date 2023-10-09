class ButtonList():
    def __init__(self, pos, buttons, orientation, dist):
        """
        An object for grouping buttons together.\n
        "orientation" indicates in which direction the list propagates. If it's equal to 0, it's horizontal, while 1 makes it vertical.\n
        "dist" is the distance in pixels between each button
        """

        self.pos = pos
        self.size = [0, 0]
        self.buttons = buttons
        self.buttons_pos = []

        self.size[orientation] = (len(buttons) - 1) * dist

        for i in range(len(buttons)):
            self.size[orientation] += buttons[i].rectangle.rect.size[orientation]

        self.size[orientation - 1] = buttons[0].rectangle.rect.size[orientation - 1]

        next_pos = [0, 0]
        next_pos[orientation] = self.pos[orientation] - self.size[orientation] / 2

        for i in range(len(buttons)):
            next_pos[orientation] += buttons[i].rectangle.rect.size[orientation] / 2

            if i != 0:
                next_pos[orientation] += dist

            # self.buttons_pos.append(next_pos)

            self.buttons[i].pos = next_pos
            self.buttons[i].rectangle.rect.center = (
                self.buttons[i].rectangle.rect.center[0] + self.pos[0],
                self.buttons[i].rectangle.rect.center[1] + self.pos[1],
            )

            for j in self.buttons[i].text.lines:
                j["pos"][0] += self.pos[0]
                j["pos"][1] += self.pos[1]
