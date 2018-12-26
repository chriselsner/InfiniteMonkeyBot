# import API keys
from keys import *

# import other libraries
import tweepy
import random
import string
import sys


# build the bot
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
bot = tweepy.API(auth)

# constants
INTERVAL = 60
CAHARACTERS = string.ascii_lowercase + " " + " " + " " + " " # 4 spaces = higher probability (the key is bigger)

# generate & post a tweet
while True:
    tweet = "".join(random.choice(chars) for i in range(280))
    bot.update_status(tweet)
    sys.sleep(INTERVAL)
