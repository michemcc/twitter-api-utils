#!/usr/bin/env python

from twitter import *

# Import twitter API credentials
import sys
sys.path.append(".")
import config

# Create the API object
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

# Create source and target users for friendship
source = ""
target = ""

# Run the API to show friendship details
result = twitter.friendships.show(source_screen_name = source,
                                  target_screen_name = target)

# Output friendship details between users
following = result["relationship"]["target"]["following"]
follows   = result["relationship"]["target"]["followed_by"]

print("%s following %s: %s" % (source, target, follows))
print("%s following %s: %s" % (target, source, following))
