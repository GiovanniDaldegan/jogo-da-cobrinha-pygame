class Text():
	def __init__(self, lines):

		self.lines = []
		self.rects = []

		for i in range(len(lines)):
			font_size = (lines[i]["font"].metrics("T")[0][1], lines[i]["font"].metrics("T")[0][3])

			pos = [
				lines[i]["pos"][0] + round(font_size[0] / 10),
				lines[i]["pos"][1] + round(font_size[1] / 5)
			]

			self.lines.append(lines[i]["font"].render(lines[i]["content"], False, lines[i]["color"]))
			self.rects.append(self.lines[i].get_rect(center = pos))
