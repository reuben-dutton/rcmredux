import os
import sys

from numpy import random

_cdir = os.path.dirname(os.path.realpath(__file__))
_bdir = os.path.join(_cdir, "..")
sys.path.append(_bdir)

import config
from memory.memory import Memory
from posting.packet import Packet
from posting.facebookposter import FacebookPoster
from posting.twitterposter import TwitterPoster
from picker.pickerManager import PickerManager, PickerType
from frames.frameManager import FrameManager, FrameType
from format.formatter import Formatter


memory = Memory()
n = random.choice(config.NUMS, p=config.DIST)

# Pick a colour picker and then get n colours
if memory.current_theme != "":
	picker = PickerManager.getPicker(PickerType.THEME, n, memory.current_theme)
else:
	picker = PickerManager.getPicker(PickerType.SCHEME|PickerType.TRUE, n)
colours = picker.getColours()

# Get a frame for n colours of a particular type
frame = FrameManager.getRandomFrame(FrameType.ALL, n)

f = Formatter(frame)

f.saveImages(colours)

packet = Packet(picker, frame, colours)

fbp = FacebookPoster()
fbp.post(packet)

tp = TwitterPoster()
tp.post(packet)