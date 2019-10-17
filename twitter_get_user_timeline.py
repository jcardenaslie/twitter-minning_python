import sys
import json
from tweepy import Cursor
from twitter_client import get_twitter_client
import time
import twitter_limit_handler as lh


if __name__ == '__main__':
	user = sys.argv[1]
	client = get_twitter_client()

	fname = "user_timeline_{}.jsonl".format(user)

	with open(fname, 'w') as f:
		for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(32):
			for status in page:
				f.write(json.dumps(status._json)+"\n")