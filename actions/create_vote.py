import os
import sys

_cdir = os.path.dirname(os.path.realpath(__file__))
_bdir = os.path.join(_cdir, '..')
sys.path.append(_bdir)

from posting.facebookposter import FacebookPoster


poster = FacebookPoster()
poster.make_vote()