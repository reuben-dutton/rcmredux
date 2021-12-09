from picker.picker import Picker
from picker.schemes.schemeReader import SchemeReader

class SchemePicker(Picker):

	ptype = "Scheme"
	subtype = "None"
	num = 0

	def __init__(self):
		self.scheme = SchemeReader.getDefault()
		self.subtype = self.scheme.name
		self.num = self.scheme.num

	def setSubtype(self, num: int, subtype: str = None):
		self.scheme = SchemeReader.getRandomScheme(num, name=subtype)
		self.subtype = self.scheme.name
		self.num = self.scheme.num

	def getColours(self):
		return self.scheme.getRandoms()