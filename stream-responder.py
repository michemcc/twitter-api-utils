#!/usr/bin/env python

from twitter import *
import time

# Define the username to match against.
username = ""

# Sleep between tweets to not flood
sleep_time = 1

# Load our API credentials
import sys
sys.path.append(".")
import config

# Create streaming API object, and standard Twitter
# object to post replies.
auth = OAuth(config.access_key,
             config.access_secret,
             config.consumer_key,
             config.consumer_secret)
twitter = Twitter(auth = auth)
stream = TwitterStream(domain = "userstream.twitter.com", auth = auth, secure = True)

# Iterate over tweets matching this filter text
tweet_iter = stream.user()

for tweet in tweet_iter:

    # Check whether this is a valid tweet
    if "entities" not in tweet:
        continue

    # Check if user is mentioned in tweet
    mentions = tweet["entities"]["user_mentions"]
    mentioned_users = [ mention["screen_name"] for mention in mentions ]

    if username in mentioned_users:
        print("thanking @%s for the mention" % tweet["user"]["screen_name"])

        # Update status with a thank you message directed at the source.
        status = "@%s thanks for the mention" % tweet["user"]["screen_name"]
        try:
            twitter.statuses.update(status = status)
        except Exception as e:
            print(" - failed (maybe a duplicate?): %s" % e)

    time.sleep(sleep_time)
