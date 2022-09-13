from os import listdir
from os.path import dirname, join, realpath

_cdir = dirname(realpath(__file__))
_bdir = join(_cdir, "..")

themeFileList = listdir(join(_bdir, 'picker', 'themes', 'data'))

with open(join(_cdir, 'themes.txt'), 'w') as f:
    for themeFile in themeFileList:
        f.write(themeFile + '\n')

