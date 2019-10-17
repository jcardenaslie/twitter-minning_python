import json
from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':
	client = get_twitter_client()

	# for page in Cursor(client.user_timeline).pages():
	# 	for status in Cursor(client.home_timeline).items(1):	    
	# 		print(page)

	with open('my_friends.jsonl', 'w') as f:
		for friend in Cursor(client.friends).items():
			f.write(json.dumps(friend._json)+"\n")

	with open('my_followers.jsonl', 'w') as f:
		for friend in Cursor(client.followers).items():
			f.write(json.dumps(friend._json)+"\n")