from dataclasses import dataclass, field
from math import hypot
from random import randint


@dataclass(init=True, repr=False, unsafe_hash=True)
class Ball:
	''' 
	Represents an open ball in 3-dimensional space. Requires a centre
	(i.e. the mean point of the ball) and a radius.
	'''

	centre: tuple[int, int, int]
	radius: float
	r: int = field(init=False)
	g: int = field(init=False)
	b: int = field(init=False)

	def __post_init__(self):
		for val in self.centre:
			if not type(val) is int:
				raise TypeError('Ball centre is not a tuple of integers.')
			if not 0 <= val <= 255:
				raise ValueError('Ball centre does not have values between 0 and 255.')
		if not type(self.radius) is float and not type(self.radius) is int:
			raise TypeError('Ball radius is not a float.')
		if not 0 < self.radius:
			raise ValueError('Ball radius is not greater than 0.')
		self.r, self.g, self.b = self.centre

	def __repr__(self):
		return f'Ball(centre={self.centre}, radius={self.radius})'

	def contains(self, point: tuple[int, int, int]) -> bool:
		if not Ball.validatePoint(point):
			return False
		rdist = self.r-point[0]
		gdist = self.g-point[1]
		bdist = self.b-point[2]
		return hypot(rdist, gdist, bdist) < self.radius

	@staticmethod
	def validatePoint(point: tuple[int, int, int]) -> bool:
		for val in point:
			if not type(val) is int:
				raise TypeError('Point is not a tuple of integers.')
			if not 0 <= val <= 255:
				return False
		return True

	@staticmethod
	def _createBall(blist: list[int, int, int, int]):
		r, g, b, ra = blist
		return Ball((r, g, b), ra)

	def getRandom(self) -> tuple[int, int, int]:
		rad, cen = self.radius, self.centre
		randc = tuple(randint(c-rad, c+rad) for c in cen)
		while not self.contains(randc):
			randc = tuple(randint(c-rad, c+rad) for c in cen)
		return randc