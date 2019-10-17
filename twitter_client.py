import os
import sys
from tweepy import API
from tweepy import OAuthHandler
 
def get_twitter_auth():
    try:
        # consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        # consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        # access_token = os.environ['TWITTER_ACCESS_TOKEN']
        # access_secret = os.environ['TWITTER_ACCESS_SECRET']
        consumer_key="yPUwHB4w481ZTVqG8eW75rbKB"
        consumer_secret="UMzWYPZOrmrSw3N9GWi5fk9f6SO9eapKXcHAZQg2HVPlCGUYzV"
        access_token="444187649-yCHYvXtk7Kb07N0gGg97aYcDDJCjm20kZK4yEqYO"
        access_secret="fesZXmuunYVtuL5QXKHtdbGYS58KzCG9W6MCcpkJoZo1b"
    
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth
 
def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client