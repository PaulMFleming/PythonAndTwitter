import json
import tweepy
from tweepy import OAuthHandler

# Set up and Authorization keys
CONSUMER_KEY = 'zIu1zNREssRYGougYYowx6FMR'
CONSUMER_SECRET = '5oGfKwcpw6z804ROBiuepycbj2Ks58G24LF7DnG4261YKptAVn'
OAUTH_TOKEN = '861653794618212353-AKK9BlHLBCcgO3Fg5pUrVLZ24g9XisN'
OAUTH_TOKEN_SECRET = 'wBickhWc05d1pMU8F49eImS9oEpKJvJHkjMuLxo4GlvXE'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

# Yahoo! Where On Earth Ids set up as constants here
DUB_WOE_ID = 560743
LON_WOE_ID = 44418
CHI_WOE_ID = 2379574

# Use the WOEIDs to get the trending topics
#in particular locations
dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
chi_trends = api.trends_place(CHI_WOE_ID)

# Loop throught the dub_trends results and
# extract the name attribute for each result,
# and then add it to a set which is assigned 
# to the dub_trends_set variable. Repeat for lon_trends
dub_trends_set = set([trend['name']
                    for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                    for trend in lon_trends[0]['trends']])
chi_trends_set = set([trend['name']
                    for trend in chi_trends[0]['trends']])

# Find trends common to two locations and return 
# results to the common_trends variable.
common_trends = set.intersection(dub_trends_set, lon_trends_set)

# Find the differing trends of two locations
# and return the results
differing_trends= set.difference(lon_trends_set, chi_trends_set)

# Print the results (format with json.dumps when necessary)
print json.dumps(dub_trends, indent=1)
print json.dumps(lon_trends, indent=1)
print "\n", common_trends
print "\n", differing_trends


