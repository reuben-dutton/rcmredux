import json
import os
import random

from picker.themes.ball import Ball
from picker.themes.theme import Theme

_cdir = os.path.dirname(os.path.realpath(__file__))

class ThemeReader:

	@staticmethod
	def loadTheme(path: str) -> str:
		try:
			with open(path, 'r') as j:
				data = json.load(j)
		except OSError:
			print('{} theme does not exist'.format(path))
			return
		return data

	@staticmethod
	def getDefault() -> Theme:
		return ThemeReader.getTheme('default')

	@staticmethod
	def getTheme(filename: str) -> Theme:
		path = os.path.join(_cdir, 'data', '{}.json'.format(filename))
		data = ThemeReader.loadTheme(path)
		return Theme._createTheme(data)

	@staticmethod
	def getRandomTheme(name: str = None) -> Theme:
		path = os.path.join(_cdir, 'data')
		themePaths = os.listdir(path)
		possThemes = []
		for item in themePaths:
			filename, _ = os.path.splitext(item)
			theme = ThemeReader.getTheme(filename)
			if theme.name == name or name == None:
				possThemes.append(theme)
		return random.choice(possThemes)