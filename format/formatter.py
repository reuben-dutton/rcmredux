
from format.painter import Painter
from format.printer import Printer
from frames.frameManager import Frame



class Formatter:

	def __init__(self, frame: Frame):
		self.frame = frame
		self.cachedColours = []
		self.cachedCleanImage = None
		self.cachedFullImage = None
		self.cached = False
		self.painter = Painter(frame)
		self.printer = Printer(frame)

	def setFrame(self, frame: Frame):
		self.frame = frame
		self.painter.setFrame(frame)
		self.printer.setFrame(frame)
		self.cached = False

	def isCached(self, colours: list[tuple[int, int, int]]):
		return self.cachedColours == colours and self.cached

	def cache(self, colours: list[tuple[int, int, int]], cleanImage, fullImage):
		self.cachedCleanImage = cleanImage 
		self.cachedFullImage = fullImage
		self.cachedColours = colours
		self.cached = True

	def getImages(self, colours: list[tuple[int, int, int]]):
		if self.isCached(colours):
			return self.cachedCleanImage, self.cachedFullImage

		cleanImage = self.painter.paintColours(colours)
		fullImage = self.printer.printNames(cleanImage)
		self.cache(colours, cleanImage, fullImage)
		return cleanImage, fullImage