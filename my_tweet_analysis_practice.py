import json
import tweepy
from tweepy import OAuthHandler
from prettytable import PrettyTable

CONSUMER_KEY = 'zIu1zNREssRYGougYYowx6FMR'
CONSUMER_SECRET = '5oGfKwcpw6z804ROBiuepycbj2Ks58G24LF7DnG4261YKptAVn'
OAUTH_TOKEN = '861653794618212353-AKK9BlHLBCcgO3Fg5pUrVLZ24g9XisN'
OAUTH_TOKEN_SECRET = 'wBickhWc05d1pMU8F49eImS9oEpKJvJHkjMuLxo4GlvXE'

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



