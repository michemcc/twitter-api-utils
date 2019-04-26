#!/usr/bin/env python

from twitter import *

import sys
import csv

# Define latitude and longitude of search
latitude = 51.474144    # geographical center of search
longitude = -0.035401    # geographical center of search
max_range = 1             # search range in kilometers
num_results = 50        # minimum results to obtain
outfile = "output.csv"

# Load our API credentials
import sys
sys.path.append(".")
import config

# Create twitter API object
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

# Open a file to write (mode "w"), and create a CSV writer object
csvfile = open(outfile, "w")
csvwriter = csv.writer(csvfile)

# Add headings to CSV file
row = [ "user", "text", "latitude", "longitude" ]
csvwriter.writerow(row)


# The twitter API only allows us to query up to 100 tweets at a time.
# To search for more, we will break our search up into 10 "pages", each
# of which will include 100 matching tweets.

result_count = 0
last_id = None
while result_count <  num_results:

    # Perform a search based on geolocation
    query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)

    for result in query["statuses"]:
        # Only process result if it has a geolocation
        if result["geo"]:
            user = result["user"]["screen_name"]
            text = result["text"]
            text = text.encode('ascii', 'replace')
            latitude = result["geo"]["coordinates"][0]
            longitude = result["geo"]["coordinates"][1]

            # Write row into CSV file
            row = [ user, text, latitude, longitude ]
            csvwriter.writerow(row)
            result_count += 1
        last_id = result["id"]

    # Let user know the location results
    print("got %d results" % result_count)

# Close file
csvfile.close()

print("written to %s" % outfile)
