import os
import sys
import json
import requests

from dotenv import find_dotenv, load_dotenv
import facepy

_cdir = os.path.dirname(os.path.realpath(__file__))
_bdir = os.path.join(_cdir, "..")
sys.path.append(_bdir)

import config
from memory.memory import Memory
from .genericposter import GenericPoster
from picker.themes.themeReader import ThemeReader

envPath = os.path.join(_cdir, 'facebook', 'facebook.env')
load_dotenv(find_dotenv(envPath))


reactions = ['LOVE', 'HAHA', 'WOW', 'SAD', 'ANGRY']

class FacebookPoster(GenericPoster):

	def __init__(self):
		self.url = 'https://graph.facebook.com/me/feed'
		self.page_id = os.environ['PAGE_ID']
		self.access_token = os.environ['FB_ACCESS_TOKEN']
		self.graph = facepy.GraphAPI(self.access_token)

	def post(self, packet):
		with open(config.FULL_PATH, 'rb') as image:
			resp = self.graph.post(path='me/photos', 
						source=image,
						published=False)
		id1 = resp['id']
		with open(config.CLEAN_PATH, 'rb') as image:
			resp = self.graph.post(path='me/photos', 
						source=image,
						published=False)
		id2 = resp['id']
		im1 = {"media_fbid":id1}
		im2 = {"media_fbid":id2}

		data = {'access_token': self.access_token,
				'message': packet.message,
				'attached_media': json.dumps([im1, im2])}

		resp = requests.post(self.url, data=data)

		# Do something with the post id later

	def make_vote(self):
		vote_themes = ThemeReader.getRandomThemes()

		theme_names = [theme.name for theme in vote_themes]

		message = vote_message.format(*theme_names)

		try:
			post_data = self.graph.post(path='me/feed', message=message)
			memory = Memory()
			memory.vote_themes = dict(zip(reactions, theme_names))
			memory.theme_vote_post_id = post_data['id']
			memory._smem()
		except Exception as e:
			print(e)
			print('Error when submitting')

	def get_vote(self):
		memory = Memory()
		post_id = memory.theme_vote_post_id
		data = self.graph.get(id=post_id, fields="reactions")
		
		results = dict()

		# Count reactions
		for react in data['reactions']['data']:
			react_type = react['type']
			results[react_type] = results.get(react_type, 0) + 1

		top_reaction = max(results, key=results.get)
		try:
			top_theme = memory.vote_themes[top_reaction]
		except:
			print('top theme is unlisted reaction')
			# Pick the first one
			top_theme = memory.vote_themes['LOVE']
		memory.current_theme = top_theme
		memory._smem()

vote_message = "-- THEME VOTE --" \
	+ "\n" \
	+ "\n" \
	+ "Vote for a theme - the highest voted theme 24 hours after this vote " \
	+ "was posted will be the theme for 3 days afterwards. The next vote " \
	+ "be in one week from now." \
	+ "\n" \
	+ u"\U0001F493" + " - " + '{}' + "\n" \
	+ u"\U0001F602" + " - " + '{}' + "\n" \
	+ u"\U0001F62E" + " - " + '{}' + "\n" \
	+ u"\U0001F622" + " - " + '{}' + "\n" \
	+ u"\U0001F620" + " - " + '{}' + "\n" \
	+ "\n" \
	+ "If you have any theme ideas, post them in the comments below <3. I " \
	+ "will try to add them to the bot when I can."