import sys
import json
from tweepy import Cursor
from twitter_client import get_twitter_client

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
