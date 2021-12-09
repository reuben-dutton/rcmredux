from PIL import Image


class Frame:

	masks: list[Image]
	heads: list[tuple[int, int]]
	bigsize: int
	smallsize: int
	wrapwidth: int
	size: tuple[int, int]
	style: str
	w: int
	h: int

	def _frameFromJson(self, data):
		self.masks = data['masks']
		self.heads = data['heads']
		self.bigsize = data['bigsize']
		self.smallsize = data['smallsize']
		self.wrapwidth = data.get('wrapwidth', 20)
		self.size = tuple(data['size'])
		self.style = data['style']
		self.name = data['name']
		self.w, self.h = data['size']

	@staticmethod
	def _createFrame(data):
		frame = Frame()
		frame._frameFromJson(data)
		return frame