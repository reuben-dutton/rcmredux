from os.path import dirname, join, realpath
import sys

from numpy.random import choice

_cdir = dirname(realpath(__file__))
_bdir = join(_cdir, "..")
sys.path.append(_bdir)

from memory.memory import Memory
from posting.packet import Packet
from posting.facebookposter import FacebookPoster
from picker.pickerManager import PickerManager, PickerType
from frames.frameManager import FrameManager, FrameType
from format.formatter import Formatter

print(_cdir)
print(_bdir)

m = Memory()
n = choice(m.nums, p=m.dist)

print(n)

# Pick a colour picker and then get n colours
picker = PickerManager.getPicker(PickerType.ALL, n)
colours = picker.getColours()

print(colours)

# Get a frame for n colours of a particular type
frame = FrameManager.getRandomFrame(FrameType.ALL, n)

print(frame)

f = Formatter(frame)

print(f)

clean, full = f.getImages(colours)

print(clean)

# Save the image
clean.save(join(_bdir, "clean.png"))
full.save(join(_bdir, "full.png"))

print('saved')

packet = Packet(picker, frame, colours)

print(packet)

fbp = FacebookPoster()
fbp.post(packet)

print('done!')