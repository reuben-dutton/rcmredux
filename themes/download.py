from json import dump
from os import listdir
from os.path import dirname, join, realpath

import DuckDuckGoImages as ddg
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.cluster import MiniBatchKMeans
from sklearn.mixture import GaussianMixture
from sklearn.cluster import DBSCAN, OPTICS


_cdir = dirname(realpath(__file__))
_bdir = join(_cdir, "..")

dl_path = join(_cdir, 'dl_images')


tc = 64
term = "gemstone black onyxes"
desc = "Cool black stone, very pretty, very expensive"
name = "Onyxes"

plot = False
save = not plot

download = False

remove_greys = False
grey_radius = 20
remove_whites = True
white_radius = 300
remove_blacks = False
black_radius = 75

double = True
triple = False

# Download images returned with a given search query
if download:
	ddg.download(term, folder=dl_path, max_urls=50, 
	         thumbnails=True, remove_folder=True)

points = np.zeros((1, 1))
weights = np.zeros((1, 1))

for image_name in listdir(dl_path):
	image_path = join(dl_path, image_name)
	try:
		image = Image.open(image_path)
	except:
		continue
	pixels = np.asarray(image)[0::10, 0::10]
	shape = pixels.shape
	w, h, l = shape
	try:
		pixels = pixels.reshape((w*h, 3))
	except:
		continue

	mix = GaussianMixture(n_components=tc, random_state=0).fit(pixels)


	if points.shape == (1, 1):
		points = mix.means_
		weights = mix.weights_
	else:
		points = np.append(points, mix.means_, axis=0)
		weights = np.append(weights, mix.weights_, axis=0)

# points = points[weights > (1/64)]
# weights = weights[weights > (1/64)]

df = pd.DataFrame(points)
dbscan = OPTICS(min_samples=2, max_eps=6.5).fit(df)

df['label'] = dbscan.labels_

centers = pd.DataFrame(index=sorted(pd.unique(dbscan.labels_)))
centers['counts'] = df['label'].value_counts()

# if len(pd.unique(dbscan.labels_)) > 8:
# 	large = centers[centers['counts'] > 2]
# else:
# 	large = centers

means = df.groupby('label').mean()
means = means.iloc[centers.index]
means = means.loc[~means.index.isin([-1])]

if double:
	dbscan = OPTICS(min_samples=5, max_eps=65).fit(means)

	means['label2'] = dbscan.labels_

	centers = pd.DataFrame(index=sorted(pd.unique(dbscan.labels_)))
	centers['counts'] = means['label2'].value_counts()

	means = means[means['label2'] != -1]
	if triple:
		dbscan = OPTICS(min_samples=5, max_eps=15).fit(means)

		means['label3'] = dbscan.labels_

		centers = pd.DataFrame(index=sorted(pd.unique(dbscan.labels_)))
		centers['counts'] = means['label3'].value_counts()

		means = means[means['label3'] != -1]

try:
	del means['label']
except:
	pass
try:
	del means['label2']
except:
	pass
try:
	del means['label3']
except:
	pass
points = means.values

actpoints = []

if remove_greys:
	for point in points:
		dists = [np.linalg.norm(point - [i, i, i]) for i in range(256)]
		if min(dists) > grey_radius:
			actpoints.append(point)
	actpoints = np.array(actpoints)
else:
	actpoints = points

newpoints = []

if remove_blacks:
	for point in actpoints:
		dist = np.linalg.norm(point - [0, 0, 0])
		if dist > black_radius:
			newpoints.append(point)
	newpoints = np.array(newpoints)
else:
	newpoints = actpoints

finpoints = []

if remove_whites:
	for point in newpoints:
		dist = np.linalg.norm(point - [255, 255, 255])
		if dist > white_radius:
			finpoints.append(point)
	finpoints = np.array(finpoints)
else:
	finpoints = newpoints


r = [point[0] for point in finpoints]
g = [point[1] for point in finpoints]
b = [point[2] for point in finpoints]

# print(counts)


if plot:
	fig = plt.figure()
	ax1=fig.add_subplot(111, projection='3d')

	# r = [point[0] for point in points]
	# g = [point[1] for point in points]
	# b = [point[2] for point in points]
	ax1.scatter(r, g, b, c=np.clip(finpoints/255, 0, 1), s=200, alpha=1, depthshade=False)

	# r = [point[0] for point in pixels[0::10000]]
	# g = [point[1] for point in pixels[0::10000]]
	# b = [point[2] for point in pixels[0::10000]]
	# ax1.scatter(r, g, b, c=pixels[0::10000]/255)

	ax1.set_xlabel('R')
	ax1.set_ylabel('G')
	ax1.set_zlabel('B')
	ax1.set_title(name)

	ax1.view_init(27,200)
	plt.show()


if save:
	data = dict()
	data['name'] = name
	data['desc'] = desc
	data['term'] = term
	balls = []
	for point in finpoints:
		clipped = np.clip(point, 0, 255)
		r, g, b = clipped
		balls.append([int(r), int(g), int(b), 5])
	data['balls'] = balls
	filename = "{}.json".format(name.lower().replace(' ', '-'))
	with open(join(_bdir, 'picker', 'themes', 'data', filename), 'w') as f:
		dump(data, f)