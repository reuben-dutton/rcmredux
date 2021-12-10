import pickle

import pandas as pd

from os.path import dirname, join, realpath

_cdir = dirname(realpath(__file__))
_bdir = join(_cdir, "..")


colourcsv = pd.read_csv(join(_cdir, "colournames.csv"), encoding='utf8')

with open(join(_cdir, 'colourKDTree.pickle'), 'rb') as f:
	colourtree = pickle.load(f)
	

def colourName(rgb):
	dist, ind = colourtree.query([rgb], k=1)
	if dist[0, 0] < 15:
		return colourcsv['name'].iloc[ind[0, 0]]
	else:
		return ''