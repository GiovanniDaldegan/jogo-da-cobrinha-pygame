class Text():
	def __init__(self, lines):
		super().__init__()
		
		self.lines = []
		self.rects = []

		for l in range(len(lines)):
			self.lines.append(lines[l]["font"].render(lines[l]["content"], False, lines[l]["color"]))
			self.rects.append(self.lines[l].get_rect(center = lines[l]["pos"]))
