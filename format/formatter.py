import os
import sys

_cdir = os.path.dirname(os.path.realpath(__file__))
_bdir = os.path.join(_cdir, "..")
sys.path.append(_bdir)

import config
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

	def saveImages(self, colours: list[tuple[int, int, int]]):
		cleanImage = self.painter.paintColours(colours)
		cleanImage.save(config.CLEAN_PATH)

		fullImage = self.printer.printNames(cleanImage)
		fullImage.save(config.FULL_PATH)