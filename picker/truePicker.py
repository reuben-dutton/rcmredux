import random

from picker.picker import Picker

class TruePicker(Picker):

	ptype = "True"
	subtype = "Random"
	num = 0

	def __init__(self):
		self.num = 1

	def setSubtype(self, num: int, subtype: str = None):
		self.num = num

	def getColours(self):
		return [self.getColour() for i in range(self.num)]

	def getColour(self):
		r, g, b = [random.randint(0, 255) for i in range(3)]
		return (r, g, b)