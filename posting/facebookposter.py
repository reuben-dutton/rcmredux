from dotenv import find_dotenv, load_dotenv
from os import environ
from os.path import dirname, join, realpath
from json import dumps
import requests

import facepy

from .genericposter import GenericPoster

_cdir = dirname(realpath(__file__))
_bdir = join(_cdir, "..")

load_dotenv(find_dotenv(join(_cdir, 'facebook', 'facebook.env')))


class FacebookPoster(GenericPoster):

	def __init__(self):
		self.image_path = join(_bdir, 'full.png')
		self.image_path2 = join(_bdir, 'clean.png')

		self.url = 'https://graph.facebook.com/me/feed'
		self.page_id = environ['PAGE_ID']
		self.access_token = environ['ACCESS_TOKEN']
		self.graph = facepy.GraphAPI(environ['ACCESS_TOKEN'])

	def post(self, packet):
		image = open(self.image_path, 'rb')
		image2 = open(self.image_path2, 'rb')
		resp = self.graph.post(path='me/photos', 
						source=image,
						published=False)
		id1 = resp['id']
		resp = self.graph.post(path='me/photos', 
						source=image2,
						published=False)
		id2 = resp['id']
		im1 = {"media_fbid":id1}
		im2 = {"media_fbid":id2}

		data = {'access_token': self.access_token,
				'message': '',
				'attached_media': dumps([im1, im2])
				}

		resp = requests.post(self.url, data=data)

		# Do something with the post id later


	def make_vote(self):
		pass

	def get_vote(self):
		pass