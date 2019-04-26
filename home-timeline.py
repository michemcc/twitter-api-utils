#!/usr/bin/env python

from twitter import *

# Load API credentials
import sys
sys.path.append(".")
import config


# Create twitter API object
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))


# Request the latest 50 tweets from people you are following
statuses = twitter.statuses.home_timeline(count = 50)
print(statuses)

# Loop through each status and print its content
for status in statuses:
    print("(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"]))
