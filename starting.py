import tweepy
import csv
import time
consumer_key="yY7t2etkOfXhMY4mLdSu1bT4e"
consumer_secret="qqjgyy7ek3alNXeR1rx4bahkZxYt6DokCR4mSWDvj36sMmuXni"
access_token="920424985197469696-bZaYinsZz3pMraXLrqTFb8ZSFkoH31L"
access_token_secret="Ss82ggBHQ4GltaasLyac28cOz5IxiXv63tqwff5vC9vxT"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	#save most recent tweets
	alltweets.extend(new_tweets)
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print ("getting tweets before %s" % (oldest))
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		#save most recent tweets
		alltweets.extend(new_tweets)
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		print ("...%s tweets downloaded so far" % (len(alltweets)))
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	pass

def followers_of(screen_name):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	allfollow = []
	page = tweepy.Cursor(api.followers, screen_name=screen_name).pages(1)
	allfollow.extend(page)
	print(allfollow[1].id)
	print(len(allfollow))
	#time.sleep(60)

	outfollow = [[fol.id, fol.screen_name] for fol in allfollow]
	with open('%s_followers.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","screen_name"])
		writer.writerows(outfollow)
	pass


'''
	while len(new_tweets) > 0:
		print ("getting tweets before %s" % (oldest))
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
		print ("...%s tweets downloaded so far" % (len(alltweets)))
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	pass
'''
#get_all_tweets("sebastianpinera")
allf=followers_of("sebastianpinera")

'''public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)

user = api.get_user('sebastianpinera')
print (user.screen_name)
print (user.followers_count)

for status in tweepy.Cursor(api.user_timeline,id="sebastianpinera").items(20):
    # process status here
    print(status)
for friend in user.friends(count = 200): ###lista de seguidores
   print (friend.screen_name)

for post in api.user_timeline(screen_name="sebastianpinera"):
		print(post.text[0])
for i in range(3):
	last_id = post.text
	for post in api.user_timeline(screen_name="sebastianpinera",max_id=last_id):
		print(post.text)
'''