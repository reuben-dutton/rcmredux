# File containing various configuration options.
import os
import sys

_cdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(_cdir)

# Image paths
CLEAN_PATH = os.path.join(_cdir, 'clean.png')
FULL_PATH = os.path.join(_cdir, 'full.png')

# Colour settings - distribution of number of colours picked
NUMS = [1, 2, 3, 4]
DIST = [0.35, 0.3, 0.2, 0.15]