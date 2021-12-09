from picker.schemes.colour import Colour


class Scheme:

	name: str
	desc: str
	num: int
	offsets: list[int]

	def getRandoms(self):
		if not self.offsets:
			raise Exception('Scheme offsets have not been defined!')

		base = Colour()
		base.setRandom()
		return [base.offset(amount).rgb for amount in self.offsets]

	def schemeFromJson(self, data):
		self.name = data['name']
		self.desc = data['desc']
		self.num = data['num']
		self.offsets = data['offsets']

	@staticmethod
	def _createScheme(data):
		scheme = Scheme()
		scheme.schemeFromJson(data)
		return scheme