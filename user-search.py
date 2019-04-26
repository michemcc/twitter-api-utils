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

# Perform a user search
results = twitter.users.search(q = '"example"')

# Loop through each of the users, and print their details
for user in results:
    print("@%s (%s): %s" % (user["screen_name"], user["name"], user["location"]))
