

class GenericPoster:

	def __init__(self):
		raise NotImplementedError

	def post(self):
		raise NotImplementedError

	def make_vote(self):
		raise NotImplementedError

	def get_vote(self):
		raise NotImplementedError