#!/usr/bin/env python

from twitter import *

# Define content of new status
new_status = "testing testing"

# Load API credentials
import sys
sys.path.append(".")
import config

# Create Twitter API object
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

# Post new status
results = twitter.statuses.update(status = new_status)
print("updated status: %s" % new_status)
