import os
import sys

from dotenv import find_dotenv, load_dotenv
import tweepy

_cdir = os.path.dirname(os.path.realpath(__file__))
_bdir = os.path.join(_cdir, "..")
sys.path.append(_bdir)

import config
from .genericposter import GenericPoster

envPath = os.path.join(_cdir, 'twitter', 'twitter.env')
load_dotenv(find_dotenv(envPath))


class TwitterPoster(GenericPoster):

	def __init__(self):
		self.client = tweepy.Client(bearer_token=os.environ['BEARER_TOKEN'],
						consumer_key=os.environ['CONSUMER_KEY'],
						consumer_secret=os.environ['CONSUMER_SECRET'],
						access_token=os.environ['TW_ACCESS_TOKEN'],
						access_token_secret=os.environ['TW_ACCESS_TOKEN_SECRET'])

		auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'],
								   os.environ['CONSUMER_SECRET'])
		auth.set_access_token(os.environ['TW_ACCESS_TOKEN'],
							  os.environ['TW_ACCESS_TOKEN_SECRET'])

		self.api = tweepy.API(auth)

	def post(self, packet):
		message = packet.message
		media = self.api.simple_upload(filename=config.FULL_PATH)
		media_id_1 = media.media_id_string
		media = self.api.simple_upload(filename=config.CLEAN_PATH)
		media_id_2 = media.media_id_string
		mIDs = [media_id_1, media_id_2]
		self.api.update_status(status=packet.message, media_ids=mIDs)

		# Do something with post id later

	def make_vote(self):
		raise NotImplementedError

	def get_vote(self):
		raise NotImplementedError

