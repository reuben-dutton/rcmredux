from json import dump, load
from os.path import dirname, join, realpath

_cdir = dirname(realpath(__file__))
_bdir = join(_cdir, "..")
_mempath = join(_cdir, 'memory.json')


class Memory(dict):

	theme: str
	scheme: str
	dist: list[int]
	nums: list[int]

	def __init__(self):
		self._lmem()

	def _lmem(self):
		with open(_mempath, 'r') as j:
			data = load(j)
			self.__dict__.update(data)

	def _smem(self):
		with open(_mempath, 'w') as j:
			j.dump(self.__dict__)