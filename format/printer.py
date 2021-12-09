from json import load
from os.path import dirname, join, realpath
from string import capwords
import textwrap as tw

from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np

from frames.frameManager import Frame
from format.formatutil import textCenter
from names.names import colourName

ImageDraw.ImageDraw.textCenter = textCenter

_cdir = dirname(realpath(__file__))
_bdir = join(_cdir, "..")

white = (255, 255, 255, 255)
black = (15, 15, 15, 255)
none = (0, 0, 0, 0)

class Printer:

	def __init__(self, frame: Frame):
		self.setFrame(frame)

	def setFrame(self, frame: Frame):
		self.frame = frame
		self.bigsize = self.frame.bigsize
		self.smallsize = self.frame.smallsize
		self.wrapwidth = self.frame.wrapwidth
		self.size = self.frame.size
		self.heads = self.frame.heads
		font_path = join(_cdir, 'fonts', 'Bayemalt-Regular.otf')
		self.bfont = ImageFont.truetype(font=font_path, size=self.bigsize)
		font_path = join(_cdir, 'fonts', 'SairaCondensed-Bold.ttf')
		self.sfont = ImageFont.truetype(font=font_path, size=self.smallsize)
		self.fontcol = (255, 255, 255, 255)

	def printNames(self, base) -> Image:
		image = base.copy()
		# Pair each name with a head location from the Frame object
		for head in self.frame.heads:
			colour = base.getpixel(head)
			hexcode = ('#%02x%02x%02x' % colour[0:3]).upper()
			name = colourName(colour[0:3]).upper()
			cHead = self.correctHead(head, base, hexcode, name)

			for i in range(2):
				blur = Image.new("RGBA", self.size, color=none)
				blurcanvas = ImageDraw.Draw(blur)
				self.textCenter(blurcanvas, cHead, hexcode, name, fill=black)
				blur = blur.filter(ImageFilter.GaussianBlur(radius=8))
				image = Image.alpha_composite(image, blur)

			front = Image.new("RGBA", self.size, color=none)
			frontcanvas = ImageDraw.Draw(front)
			self.textCenter(frontcanvas, cHead, hexcode, name, fill=white)
			image = Image.alpha_composite(image, front)

		return image

	def getBoxSize(self, image, hexcode, name):
		canvas = ImageDraw.Draw(image)
		hexcodeW, hexcodeH = canvas.textsize(hexcode, self.bfont)

		namelines = tw.wrap(name, width=self.wrapwidth)
		nameW, nameH = 0, 0
		for line in namelines:
			lw, lh = canvas.textsize(line, self.sfont)
			nameW = max(lw, nameW)
			nameH += 5*lh/6

		w = max(hexcodeW, nameW)
		h = 5*hexcodeH/6 + 3*nameH/3

		return (w, h)

	def correctHead(self, head, image, hexcode, name):
		boxW, boxH = self.getBoxSize(image, hexcode, name)
		baseW, baseH = image.size
		currentX, currentY = head
		marginX, marginY = int(baseW/25), int(baseH/25)
		# marginX, marginY = 0, 0

		if currentX >= marginX and currentX <= baseW - marginX:
			marginX = 0

		if currentY >= marginY and currentY <= baseH - marginY:
			marginY = 0


		if currentX + boxW/2 + marginX >= baseW:
			currentX = baseW - boxW/2 - marginX
		if currentX - boxW/2 - marginX <= 0:
			currentX = boxW/2 + marginX

		if currentY + boxH/2 + marginY >= baseH:
			currentY = baseH - boxH/2 - marginY
		if currentY - boxH/2 - marginY <= 0:
			currentY = boxH/2 + marginY

		return (currentX, currentY)

	def textCenter(self, canvas, head, hexcode, name, fill=None):
		x, y = head

		# # Get the dimensions of the text
		hexcodeW, hexcodeH = canvas.textsize(hexcode, self.bfont)

		namelines = tw.wrap(name, width=self.wrapwidth)
		nameW, nameH = 0, 0
		namexs = []
		nameys = []
		for line in namelines:
			lw, lh = canvas.textsize(line, self.sfont)
			nameW = max(lw, nameW)
			nameH += 5*lh/6
			namexs.append(x - lw/2)

		h = 5*hexcodeH/6 + 3*nameH/3

		for i in range(len(namexs)):
			nameys.append(y - h/2 + i*nameH/len(namexs))

		hexx = x - hexcodeW/2
		if len(nameys) > 0:
			hexy = nameys[0] + nameH - hexcodeH/6
		else:
			hexy = y - h/2 + nameH - hexcodeH/6
		
		for i in range(len(namelines)):
			line = namelines[i]
			namex = namexs[i]
			namey = nameys[i]
			canvas.text((namex, namey), line, font=self.sfont, fill=fill)

		canvas.text((hexx, hexy), hexcode, font=self.bfont, fill=fill)
