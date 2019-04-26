#!/usr/bin/env python

from twitter import *
from datetime import datetime

created_at_format = '%a %b %d %H:%M:%S +0000 %Y'

# Load API credentials
import sys
sys.path.append(".")
import config

# Create API object
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

# Define search criteria
terms = "pink elephants"
query = twitter.search.tweets(q = terms)
results = query["statuses"]

# Take timestamp of the first and last tweets in these results,
# and calculate the average time between tweets.
first_timestamp = datetime.strptime(results[0]["created_at"], created_at_format)
last_timestamp = datetime.strptime(results[-1]["created_at"], created_at_format)
total_dt = (first_timestamp - last_timestamp).total_seconds()
mean_dt = total_dt / len(results)

# Print the average of the differences
print("Average tweeting rate for '%s' between %s and %s: %.3fs" % (terms, results[-1]["created_at"], results[ 0]["created_at"], mean_dt))
