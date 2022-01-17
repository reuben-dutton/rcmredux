import os
import sys

_cdir = os.path.dirname(os.path.realpath(__file__))
_bdir = os.path.join(_cdir, '..')
sys.path.append(_bdir)

from memory.memory import Memory


memory = Memory()
memory.current_theme = ""
memory._smem()