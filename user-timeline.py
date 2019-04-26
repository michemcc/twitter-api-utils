#!/usr/bin/env python

from twitter import *

# Load API credentials
import sys
sys.path.append(".")
import config

# Create API object
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

# Define user to query
user = ""

# Query the user timeline
results = twitter.statuses.user_timeline(screen_name = user)

# Loop through each status item and print its content.
for status in results:
    print("(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore")))
