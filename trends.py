#!/usr/bin/env python

from twitter import *

# Load our API credentials
import sys
sys.path.append(".")
import config

# Create API object
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

# Retrieve global trends with id=1, other Yahoo Where on Earth id's at:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://developer.twitter.com/en/docs/trends/trends-for-location/api-reference/get-trends-place
results = twitter.trends.place(_id = 1)

print("Global Trends")

for location in results:
    for trend in location["trends"]:
        print(" - %s" % trend["name"])
