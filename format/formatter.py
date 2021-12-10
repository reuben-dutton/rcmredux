
from format.painter import Painter
from format.printer import Printer
from frames.frameManager import Frame



class Formatter:

	def __init__(self, frame: Frame):
		self.frame = frame
		self.painter = Painter(frame)
		self.printer = Printer(frame)

	def setFrame(self, frame: Frame):
		self.frame = frame
		self.painter.setFrame(frame)
		self.printer.setFrame(frame)

	def getImages(self, colours: list[tuple[int, int, int]]):
		cleanImage = self.painter.paintColours(colours)
		fullImage = self.printer.printNames(cleanImage)
		return cleanImage, fullImage