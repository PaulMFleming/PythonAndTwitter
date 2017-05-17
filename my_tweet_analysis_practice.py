import json
import tweepy
from tweepy import OAuthHandler
from prettytable import PrettyTable
from settings import twitter_app_config

CONSUMER_KEY = twitter_app_config.get('CONSUMER_KEY')
CONSUMER_SECRET = twitter_app_config.get('CONSUMER_SECRET')
OAUTH_TOKEN = twitter_app_config.get('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = twitter_app_config.get('OAUTH_TOKEN_SECRET')

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 100
query = 'Cohen'

# Get all stats
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

# Print the following attributes:
for status in results:
    print "Name:\t", status.user.name.encode('utf-8'), "\n"
    print "Description:\t", status.user.description.encode('utf-8'), "\n"
    print "Location:\t", status.user.location.encode('utf-8'), "\n"
    print "Time Zone:\t", status.user.time_zone, "\n"

# Print the same as above using PrettyTable to format the results

table = PrettyTable(field_names=[label, 'Name'])
[ table.add_row(entry) for entry in status.user.name.encode('utf-8') ]
table.align[label] = 'l'
print table

