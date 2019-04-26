#!/usr/bin/env python

from twitter import *
import re

# Define search term
search_term = "bieber"

# Import a load of external features, for text display and date handling
# you will need the termcolor module: pip install termcolor

from time import strftime
from textwrap import fill
from termcolor import colored
from email.utils import parsedate

# Load API credentials
import sys
sys.path.append(".")
import config

# Create streaming API object
auth = OAuth(config.access_key,
             config.access_secret,
             config.consumer_key,
             config.consumer_secret)
stream = TwitterStream(auth = auth, secure = True)

# Iterate over tweets matching this filter text
tweet_iter = stream.statuses.filter(track = search_term)

pattern = re.compile("%s" % search_term, re.IGNORECASE)

for tweet in tweet_iter:
    # Turn the date string into a date object that python can handle
    timestamp = parsedate(tweet["created_at"])

    # Now format this nicely into HH:MM:SS format
    timetext = strftime("%H:%M:%S", timestamp)

    # Color our tweet's time, user and text
    time_colored = colored(timetext, color = "white", attrs = [ "bold" ])
    user_colored = colored(tweet["user"]["screen_name"], "green")
    text_colored = tweet["text"]

    # Replace each instance of search terms with a highlighted version
    text_colored = pattern.sub(colored(search_term.upper(), "yellow"), text_colored)

    # Add indenting to each line and wrap the text
    indent = " " * 11
    text_colored = fill(text_colored, 80, initial_indent = indent, subsequent_indent = indent)

    # Output tweet
    print("(%s) @%s" % (time_colored, user_colored))
    print("%s" % (text_colored))
