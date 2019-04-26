#!/usr/bin/env python

from twitter import *

# Load API credentials
import sys
sys.path.append(".")
import config

# Create twitter streaming API object
auth = OAuth(config.access_key,
             config.access_secret,
             config.consumer_key,
             config.consumer_secret)
stream = TwitterStream(auth = auth, secure = True)

# Iterate over tweets matching this filter text
tweet_iter = stream.statuses.filter(track = "social")

for tweet in tweet_iter:

    # Print out the contents, and any URLs found inside
    # Prints live results containing a URL link and the #OWS tag
    print("(%s) @%s %s" % (tweet["created_at"], tweet["user"]["screen_name"], tweet["text"]))
    for url in tweet["entities"]["urls"]:
        print(" - found URL: %s" % url["expanded_url"])
