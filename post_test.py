import os
import sys

from numpy import random

_cdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(_cdir)

import config
from memory.memory import Memory
from posting.packet import Packet
from posting.twitterposter import TwitterPoster
from picker.pickerManager import PickerManager, PickerType
from frames.frameManager import FrameManager, FrameType
from format.formatter import Formatter


memory = Memory()
n = random.choice(config.NUMS, p=config.DIST)

# Pick a colour picker and then get n colours
picker = PickerManager.getPicker(PickerType.SCHEME|PickerType.TRUE, n)
colours = picker.getColours()

# Get a frame for n colours of a particular type
frame = FrameManager.getRandomFrame(FrameType.ALL, n)

f = Formatter(frame)

f.saveImages(colours)

packet = Packet(picker, frame, colours)

poster = FacebookPoster()
poster.post(packet)
