from dataclasses import dataclass, field
from enum import IntFlag
from json import load
from os import listdir, walk
from os.path import dirname, isfile, join, realpath
from random import choice

from PIL import Image

from frames.frame import Frame

_cdir = dirname(realpath(__file__))
_bdir = join(_cdir, "..")

pathmap = {1: ["default"],
		   2: ["gradient"],
		   3: ["default", "gradient"],
		   4: ["palette"],
		   5: ["default", "palette"],
		   6: ["gradient", "palette"],
		   7: ["default", "gradient", "palette"]}

class FrameType(IntFlag):
	DEFAULT = 1
	GRADIENT = 2
	PALETTE = 4
	ALL = 7

class FrameManager:

	@staticmethod
	def getFrame(frame: str) -> Frame:
		path = join(_cdir, frame)
		return FrameManager.loadFrame(path)

	@staticmethod
	def loadFrame(path: str) -> Frame:
		# Get all files in the folder
		files = [join(path, name) for name in listdir(path)]
		# Filter out non-image files (these are masks)
		image_files = [f for f in files if f.endswith('.png')]
		# Load all mask image files
		masks = [Image.open(imgf).convert('RGBA') for imgf in image_files]

		data = FrameManager.getFrameJson(path)
		data['heads'] = [tuple(item) for item in data['heads']]

		data['masks'] = masks
		return Frame._createFrame(data)

	@staticmethod
	def getRandomFrame(frameType: FrameType, num: list[int], name: str = None) -> Frame:
		typefolders = pathmap[frameType]
		# Revert to default if number of colours is 1
		if num == 1:
			typefolders = pathmap[1]
		possframepaths = []
		for typefolder in typefolders:
			top = join(_cdir, typefolder)
			for root,dirs,files in walk(top):
				if not dirs and files:
					data = FrameManager.getFrameJson(root)
					if data['num'] == num and (data['name'] == name or name == None):
						possframepaths.append(root)

		if not possframepaths:
			raise Exception('No frame fits the given requirements.')
		randompath = choice(possframepaths)
		return FrameManager.loadFrame(randompath)

	@staticmethod
	def getFrameJson(path):
		with open(join(path, 'frame.json'), 'r') as j:
			return load(j)


		
