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

# Define username of Twitter user
username = ""

# Search for friends usernames
query = twitter.friends.ids(screen_name = username)

# Determine quantity of friends/search results
print("Found %d friends\n" % (len(query["ids"])))

# Order results into blocks of 100
for n in range(0, len(query["ids"]), 100):
    ids = query["ids"][n:n+100]

    # Create a comma-separated string from the ID list
    ids_string = ",".join(str(id) for id in ids)

    # Obtain other information about the users using subquery
    subquery = twitter.users.lookup(user_id = ids_string)

    for user in subquery:
        # Print out users, with star if verified
        print(" [%s] %s - %s" % ("*" if user["verified"] else " ", user["screen_name"], user["location"]))
