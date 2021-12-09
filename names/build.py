from ast import literal_eval

import pandas as pd
import numpy as np
from sklearn.neighbors import KDTree

import pickle

colourcsv = pd.read_csv("names/colournames.csv", encoding='utf8')

colourcsv['rgb'] = colourcsv['rgb'].apply(literal_eval)
colourcsv['rgb'] = colourcsv['rgb'].apply(list)

array = list(colourcsv['rgb'].to_numpy())

tree = KDTree(array)

with open('names/colourKDTree.pickle', 'wb') as f:
	pickle.dump(tree, f)

# with open('names/colourKDTree.pickle', 'rb') as f:
# 	colourtree = pickle.load(f)


# dist, ind = colourtree.query([[145, 80, 200]], k=1)
# print(ind)
# print(dist)

# print(colourcsv.iloc[ind[0, 0]])