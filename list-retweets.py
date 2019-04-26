#!/usr/bin/env python

from twitter import *

# Initialize user
user = ""

# Load API credentials
import sys
sys.path.append(".")
import config

# Create twitter API object
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

# Perform a basic search
results = twitter.statuses.user_timeline(screen_name = user)

# Loop through each of status and print its content
for status in results:
    print("@%s %s" % (user, status["text"]))

    # Print users who have retweeted this tweet
    retweets = twitter.statuses.retweets._id(_id = status["id"])
    for retweet in retweets:
        print(" - retweeted by %s" % (retweet["user"]["screen_name"]))
