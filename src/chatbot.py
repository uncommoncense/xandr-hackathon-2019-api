import os
from mastodon import Mastodon


class MastodonBot(object):
    def __init__(self):
        self._mastodon = Mastodon(
            access_token=os.environ['MASTODON_ACCESS_TOKEN'],
            api_base_url=os.environ['MASTODON_BASE_URL']
        )

        self._mastodon.log_in(
            username=os.environ['MASTODON_USERNAME'],
            password=os.environ['MASTODON_PASSWORD']
        )

    def reply_to(self, original_status_id):
        self._mastodon.status_post(
            status="Not cool",
            in_reply_to_id=original_status_id,
            visibility="private"
        )


if __name__ == '__main__':
    bot = MastodonBot()
