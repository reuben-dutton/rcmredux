from dotenv import find_dotenv, load_dotenv
from os import environ
from os.path import dirname, join, realpath

import tweepy

from .genericposter import GenericPoster

_cdir = dirname(realpath(__file__))
_bdir = join(_cdir, "..")

load_dotenv(find_dotenv(join(_cdir, 'twitter', 'twitter.env')))


class TwitterPoster(GenericPoster):

	def __init__(self):
		self.image_path = join(_bdir, 'full.png')
		self.client = tweepy.Client(bearer_token=environ['BEARER_TOKEN'],
						consumer_key=environ['CONSUMER_KEY'],
						consumer_secret=environ['CONSUMER_SECRET'],
						access_token=environ['ACCESS_TOKEN'],
						access_token_secret=environ['ACCESS_TOKEN_SECRET'])

		auth = tweepy.OAuthHandler(environ['CONSUMER_KEY'],
								   environ['CONSUMER_SECRET'])
		auth.set_access_token(environ['ACCESS_TOKEN'],
							  environ['ACCESS_TOKEN_SECRET'])

		self.api = tweepy.API(auth)

	def post(self, packet):
		message = packet.message
		media = self.api.simple_upload(filename=self.image_path)
		return media

	def make_vote(self):
		raise NotImplementedError

	def get_vote(self):
		raise NotImplementedError

