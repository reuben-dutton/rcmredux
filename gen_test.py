import os
import sys

_cdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(_cdir)

from posting.facebookposter import FacebookPoster


poster = FacebookPoster()
poster.get_vote()