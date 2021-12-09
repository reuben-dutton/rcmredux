from colorsys import hls_to_rgb, rgb_to_hls
from dataclasses import dataclass
from random import random

def clamp(value, minvalue, maxvalue):
	return max(min(value, maxvalue), minvalue)

@dataclass(init=False, repr=False, unsafe_hash=True)
class Colour:

	hue: float
	sat: float
	light: float

	def __init__(self):
		self.hue = 0
		self.sat = 1
		self.light = 0.5

	def __repr__(self):
		return f'hsv({self.hue}, {self.sat}, {self.light})'

	def setRandom(self):
		r, g, b = [random() for i in range(3)]
		h, l, s = rgb_to_hls(r, g, b)
		self.hue = h*360
		self.sat = s
		self.light = l

	@property
	def rgb(self):
		r, g, b = hls_to_rgb(self.hue/360, self.light, self.sat)
		return (int(r*255), int(g*255), int(b*255))

	def offset(self, degrees):
		newColour = Colour()
		newColour.hue = self.hue + degrees
		# newColour.sat = self.sat
		newColour.sat = random()
		# newColour.light = self.light
		newColour.light = random()
		return newColour

