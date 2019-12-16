from mastodon import Mastodon
import os

"""Simple test script that posts something from a test account"""


# imports access token and api base url from environment
mastodon = Mastodon(
	access_token=os.environ['API_TOKEN'],
	api_base_url=os.environ['API_BASE']
)

mastodon.log_in(
	'test@gmail.com',
	'asdf1234'
)

mastodon.toot("Hello guys, welcome to my Minecraft let's play!")