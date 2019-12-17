from test_mastodon import create_and_log_in
import requests


if __name__=='__main__':
	# also testing reporting a message as toxic
	mastodon = create_and_log_in()

	toot_dict = mastodon.toot("[Test] This is a toxic message.")

	url = f"http://127.0.0.1:8000/report/@test1337/{toot_dict['id']}"

	requests.get(url)
	print("Reporting user @test1337...")
	