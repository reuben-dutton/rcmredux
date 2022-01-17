from PIL import Image

from frames.frame import Frame
from picker.picker import Picker

class Packet:

	def __init__(self, picker, frame, colours):
		self.picker = picker
		self.frame = frame
		self.colours = colours

	@property
	def message(self):
		if self.picker.ptype == "Theme":
			return f"Themed - {self.picker.subtype}"
		return ""