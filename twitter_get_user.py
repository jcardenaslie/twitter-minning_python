import os
import sys
import json
import time
import math
import csv
from tweepy import Cursor
from twitter_client import get_twitter_client

MAX_FRIENDS = 5000

def usage():
	print("Usage:")
	print("python {} <username>".format(sys.argv[0]))

def paginate(items, n):
	"""Generate n-sized chunks from items"""
	for i in range(0, len(items), n):
		yield items[i:i+n]

def get_info(twitter_user):
	# screen_name = sys.argv[1]
	screen_name = twitter_user
	client = get_twitter_client()
	dirname = "users/{}".format(screen_name)
	max_pages = math.ceil(MAX_FRIENDS / 5000)

	try:
		os.makedirs(dirname, mode=0o755, exist_ok=True)
	except OSError:
		print("Directory {} already exists".format(dirname))
	except Exception as e:
		print("Error while creating directory{}".format(dirname))
		print(e)
		sys.exit(1)

	print('Extrayendo a {} \n'.format(screen_name))

	# get followers for a given user
	fjson = "users/{}/followers.jsonl".format(screen_name)
	fcsv = "users/{}/followers.csv".format(screen_name)

	with open(fjson, 'w') as f1, open(fcsv, 'w') as f2:
		for followers in Cursor(client.followers_ids,screen_name=screen_name).pages(max_pages):
			for chunk in paginate(followers, 100):
				users = client.lookup_users(user_ids=chunk)
				
				# out = [[user.created_at, user.id, user.screen_name,user.name, user.description, user.location] for user in users]
				out = [[user.id, user.screen_name] for user in users]
				writer = csv.writer(f2)
				writer.writerow(["id","screen_name"])
				writer.writerows(out)
				
				for user in users:
					f1.write(json.dumps(user._json)+"\n")
			if len(followers) == 5000:
				print("Followers: More results available. Sleeping for 60seconds to avoid rate limit")
				time.sleep(60)

	# get friends for a given user
	fjson = "users/{}/friends.jsonl".format(screen_name)
	fcsv = "users/{}/friends.csv".format(screen_name)

	with open(fjson, 'w') as f1, open(fcsv, 'w') as f2:
		for friends in Cursor(client.friends_ids,screen_name=screen_name).pages(max_pages):
			for chunk in paginate(friends, 100):
				users = client.lookup_users(user_ids=chunk)
				
				# out = [[user.created_at, user.id, user.screen_name,user.name, user.description, user.location] for user in users]
				# writer = csv.writer(f2)
				# writer.writerow(["id","screen_name"])
				# writer.writerows(out)

				for user in users:
					
					f1.write(json.dumps(user._json)+"\n")
			if len(friends) == 5000:
				print("Friends: More results available. Sleeping for 60 seconds to avoid rate limit")
				time.sleep(60)
	
	# get user's profile
	fname ="users/{}/user_profile.json".format(screen_name)	
	with open(fname, 'w') as f:
		profile = client.get_user(screen_name=screen_name)
		f.write(json.dumps(profile._json, indent=4))

if __name__ == '__main__':
	# if len(sys.argv) != 2:
	# 	usage()
	# 	sys.exit(1)

	candidatos = ["sebastianpinera",
	"marcoporchile",
	"Guillier2018",
	"BeaSanchezYTu",
	"eduardo_artes",
	"joseantoniokast",
	"carolinagoic",
	"navarrobrain"
	]
	for candidato in candidatos:
		get_info(candidato)
	
