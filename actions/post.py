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


m = Memory()
n = choice(m.nums, p=m.dist)

# Pick a colour picker and then get n colours
picker = PickerManager.getPicker(PickerType.ALL, n)
colours = picker.getColours()

# Get a frame for n colours of a particular type
frame = FrameManager.getRandomFrame(FrameType.ALL, n)

f = Formatter(frame)

f.saveImages(colours, _bdir)

packet = Packet(picker, frame, colours)

fbp = FacebookPoster()
fbp.post(packet)