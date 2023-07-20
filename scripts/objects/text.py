class Text():
	def __init__(self, lines):

		self.lines = []
		self.rects = []

		for i in range(len(lines)):
			self.lines.append(lines[i]["font"].render(lines[i]["content"], False, lines[i]["color"]))
			self.rects.append(self.lines[i].get_rect(center = lines[i]["pos"]))
