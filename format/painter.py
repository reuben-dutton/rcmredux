from PIL import Image
import numpy as np

from frames.frameManager import Frame

zero = (0, 0, 0, 0)

resmap = {"gradient": Image.ANTIALIAS,
		  "palette": Image.NEAREST,
		  "default": Image.ANTIALIAS}

import psutil

class Painter:

	def __init__(self, frame: Frame):
		self.setFrame(frame)

	def setFrame(self, frame: Frame):
		self.frame = frame
		self.size = self.frame.size
		self.resample = resmap[self.frame.style]

	def paintColours(self, colours: list[tuple[int, int, int]]) -> Image:

		# Get an empty image (0, 0, 0, 0) and convert to numpy array
		base = np.float64(np.asarray(Image.new("RGBA", self.size, color=zero)))

		# Pair each colour with a mask from the Frame object
		for (colour, mask) in zip(colours, self.frame.masks):

			# Resize the mask to the full image size
			fullmask = mask.resize(self.size, resample=self.resample)

			# Convert the mask to a numpy array
			maskarray = np.asarray(fullmask)

			# Convert the colour to a (R, G, B, A) tuple
			fullcolour = tuple(list(colour) + [255])

			# Create a full colour image using the (R, G, B, A) tuple
			overlay = np.asarray(Image.new("RGBA", self.size, color=fullcolour))
			overlay = overlay.copy()
			# Get the alpha channel of the mask array
			alpha = maskarray[:, :, 3]

			# Tile the array so we have an array in (A, A, A, A) format
			maskalpha = alpha[:, :, np.newaxis]
			maskalpha = np.tile(maskalpha, (1, 1, 4))/255

			# Set the alpha channel to 1
			maskalpha[:, :, 3] = np.ones(alpha.shape)

			# Set the full colour image alpha to the mask alpha values
			overlay[:, :, 3] = alpha

			# Multiply the full colour image by the alpha values and paste
			# on top of the current base image.
			base = base + overlay*maskalpha


		# Sanity check - print the highest and lowest alpha value
		# print(np.amax(base[:, :, 3]))
		# print(np.amin(base[:, :, 3]))

		# Convert the final numpy array to an Image object
		result = Image.fromarray(base.astype(np.uint8))

		# Set all alpha values to 255 (fully opaque)
		result.putalpha(255)


		return result