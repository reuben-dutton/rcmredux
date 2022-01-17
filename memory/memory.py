import os
import json

_cdir = os.path.dirname(os.path.realpath(__file__))
_bdir = os.path.join(_cdir, "..")
_mempath = os.path.join(_cdir, 'memory.json')


class Memory(dict):

	current_theme: str
	vote_themes: list[str]
	theme_vote_post_id: str

	def __init__(self):
		self._lmem()

	def _lmem(self):
		with open(_mempath, 'r') as j:
			data = json.load(j)
			self.__dict__.update(data)

	def _smem(self):
		with open(_mempath, 'w') as j:
			json.dump(self.__dict__, j)