#!/usr/bin/env python

from twitter import *

# Create the list of users that we want to examine

users = [ "", "", "" ]

# Load our API credentials

import sys
sys.path.append(".")
import config

# Create twitter API object

twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

# For each user in the list, retrieve the lists they own

import pprint
for user in users:
    print("@%s" % (user))

    result = twitter.lists.list(screen_name = user)
    for list in result:
        print(" - %s (%d members)" % (list["name"], list["member_count"]))
