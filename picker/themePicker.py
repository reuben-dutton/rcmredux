from picker.picker import Picker
from picker.themes.themeReader import ThemeReader

class ThemePicker(Picker):

	ptype = "Theme"
	subtype = "None"
	num = 0

	def __init__(self):
		self.theme = ThemeReader.getDefault()
		self.subtype = self.theme.name
		self.num = 1

	def setSubtype(self, num: int, subtype: str = None):
		self.theme = ThemeReader.getRandomTheme(name=subtype)
		self.subtype = self.theme.name
		self.num = num

	def getColours(self):
		return self.theme.getRandoms(self.num)