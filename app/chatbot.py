import os
import json
from datetime import date,datetime
from mastodon import Mastodon


TOXIC_ALERT = (
    "\U000026A0 Warning! \U000026A0 \n"
    "\nThis post has been marked as toxic by the AdminBot. Consider being nicer next time."
)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


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

    def reply_to(self, user, original_status_id):
        return json.dumps(self._mastodon.status_post(
            status=user + " " + TOXIC_ALERT,
            in_reply_to_id=original_status_id,
            visibility="direct",
            idempotency_key="Bot-" + str(original_status_id)
        ), cls=ComplexEncoder)


if __name__ == '__main__':
    bot = MastodonBot()
