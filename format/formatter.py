from os.path import join

from format.painter import Painter
from format.printer import Printer
from frames.frameManager import Frame

import psutil

class Formatter:

	def __init__(self, frame: Frame):
		self.frame = frame
		self.painter = Painter(frame)
		self.printer = Printer(frame)

	def setFrame(self, frame: Frame):
		self.frame = frame
		self.painter.setFrame(frame)
		self.printer.setFrame(frame)

	def saveImages(self, colours: list[tuple[int, int, int]], path: str):
		cleanImage = self.painter.paintColours(colours)
		cleanImage.save(join(path, "clean.png"))

		fullImage = self.printer.printNames(cleanImage)
		fullImage.save(join(path, "full.png"))