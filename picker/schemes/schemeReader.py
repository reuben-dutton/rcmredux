import json
import os
import random

from picker.schemes.scheme import Scheme

_cdir = os.path.dirname(os.path.realpath(__file__))

class SchemeReader:

	@staticmethod
	def loadScheme(path: str) -> str:
		try:
			with open(path, 'r') as j:
				data = json.load(j)
		except OSError:
			print('{} scheme does not exist'.format(path))
			return
		return data

	@staticmethod
	def getDefault():
		return SchemeReader.getScheme('default')

	@staticmethod
	def getScheme(filename: str) -> Scheme:
		path = os.path.join(_cdir, 'data', '{}.json'.format(filename))
		data = SchemeReader.loadScheme(path)
		return Scheme._createScheme(data)

	@staticmethod
	def getRandomScheme(num: int, name: str = None) -> Scheme:
		path = os.path.join(_cdir, 'data')
		schemePaths = os.listdir(path)
		possSchemes = []
		for item in schemePaths:
			filename, _ = os.path.splitext(item)
			scheme = SchemeReader.getScheme(filename)
			if scheme.num == num and (scheme.name == name or name == None):
				possSchemes.append(scheme)
		return random.choice(possSchemes)