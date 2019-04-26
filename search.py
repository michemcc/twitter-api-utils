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

# Define criteria for search
query = twitter.search.tweets(q = "lazy dog")

# Print duration of search
print("Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"]))

# Loop through each of the results, and print its content.
for result in query["statuses"]:
    print("(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"]))
