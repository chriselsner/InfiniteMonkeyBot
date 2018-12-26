# import Twitter API keys
from keys import *

# import other libraries
import tweepy
import random
import string


# build the bot
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
bot = tweepy.API(auth)

# generate tweet
chars = string.ascii_lowercase + " "
tweet = "".join(random.choice(chars) for i in range(280))

# post tweet
bot.update_status(tweet)
