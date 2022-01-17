from random import choices, randint, random

from picker.themes.ball import Ball

class Theme:

	def __init__(self):
		self.name = ""
		self.desc = ""
		self.balls = set()

	def __repr__(self):
		return f'Theme(name={self.name})'

	def add(self, ball: Ball):
		self.balls.add(ball)

	def remove(self, ball: Ball):
		self.balls.remove(ball)

	def contains(self, point: tuple[int, int, int]) -> bool:
		result = False
		for ball in self.balls:
			result = result or ball.contains(point)
		return result

	def getRandom(self) -> tuple[int, int, int]:
		dist = [ball.radius**2 for ball in self.balls]
		ball = choices(list(self.balls), weights=dist)[0]
		rand = None
		while rand == None:
			rand = ball.getRandom()
			others = sum([other.contains(rand) for other in self.balls])
			if random() > 1/others:
				rand = None
				ball = choices(list(self.balls), weights=dist)[0]
		return rand

	def getRandoms(self, num: int) -> list[tuple[int, int, int]]:
		return [self.getRandom() for i in range(num)]

	def themeFromJson(self, data: dict):
		self.name = data['name']
		self.desc = data['desc']
		for blist in data['balls']:
			self.add(Ball._createBall(blist))

	@staticmethod
	def _createTheme(data: dict):
		theme = Theme()
		theme.themeFromJson(data)
		return theme


