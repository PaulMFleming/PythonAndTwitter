import json
import tweepy
from tweepy import OAuthHandler
from prettytable import PrettyTable
from collections import Counter
from operator import itemgetter
from settings import twitter_app_config


CONSUMER_KEY = twitter_app_config.get('CONSUMER_KEY')
CONSUMER_SECRET = twitter_app_config.get('CONSUMER_SECRET')
OAUTH_TOKEN = twitter_app_config.get('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = twitter_app_config.get('OAUTH_TOKEN_SECRET')


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 150
query = 'Ireland'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

# controls how many retweets a tweet 
# needs in order to be considered popular
min_retweets = 10 

# loops through results to determine if a tweet is popular
# if it is it's added to the pop_tweets list
pop_tweets = [ status
            for staus in results
            if status._json['retweet_count'] > min_retweets ]

# create a list of tweet tuples associating each 
# tweet's text with it's retweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), 
                tweet._json['retweet_count'])
                for tweet in pop_tweets]

# sort the tuple entries in descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# prettify 
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r' # align colums
print table