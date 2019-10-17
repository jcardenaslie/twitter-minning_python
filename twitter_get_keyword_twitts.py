# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The search term you want to find
query = "Toptal"
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print(tweet.user.screen_name,"Tweeted:",tweet.text)