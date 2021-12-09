import math
import textwrap as tw


def textCenter(self, head, big, small, wrapwidth, fill=None):
	''' Take a point (x, y), below or above, some text, and an ImageDraw object.
		Center the text at the given point and place it on the
		ImageDraw object.
	'''
	x, y = head

	hexcode, bfont = big
	name, sfont = small

	# # Get the dimensions of the text
	hexcodeW, hexcodeH = self.textsize(hexcode, bfont)

	namelines = tw.wrap(name, width=wrapwidth)
	nameW, nameH = 0, 0
	namexs = []
	nameys = []
	for line in namelines:
		lw, lh = self.textsize(line, sfont)
		nameW = max(lw, nameW)
		nameH += 5*lh/6
		namexs.append(x - lw/2)

	h = 5*hexcodeH/6 + 3*nameH/3

	for i in range(len(namexs)):
		nameys.append(y - h/2 + i*nameH/len(namexs))

	hexx = x - hexcodeW/2
	hexy = nameys[0] + nameH - hexcodeH/6
	
	for i in range(len(namelines)):
		line = namelines[i]
		namex = namexs[i]
		namey = nameys[i]
		self.text((namex, namey), line, font=sfont, fill=fill)

	self.text((hexx, hexy), hexcode, font=bfont, fill=fill)