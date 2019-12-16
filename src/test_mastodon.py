from argparse import ArgumentParser
from mastodon import Mastodon
import os

"""Simple test script that posts something from a test account"""


def create_and_log_in():
	# imports access token and api base url from environment
	mastodon = Mastodon(
		access_token=os.environ['MASTODON_ACCESS_TOKEN'],
		api_base_url=os.environ['MASTODON_BASE_URL']
	)

	mastodon.log_in(
		'test@gmail.com',
		'asdf1234'
	)

	return mastodon

if __name__ == '__main__':
	parser = ArgumentParser(description='Simple Test CLI tool that toots in mastodon')
	parser.add_argument("-p", type=str, help="status you want to toot", required=True)
	args = parser.parse_args()

	mastodon = create_and_log_in()
	mastodon.toot(args.p)
