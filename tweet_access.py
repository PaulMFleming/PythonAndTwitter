import json
import tweepy
from tweepy import OAuthHandler
from settings import twitter_app_config

CONSUMER_KEY = twitter_app_config.get('CONSUMER_KEY')
CONSUMER_SECRET = twitter_app_config.get('CONSUMER_SECRET')
OAUTH_TOKEN = twitter_app_config.get('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = twitter_app_config.get('OAUTH_TOKEN_SECRET')

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 10
query = 'Dublin'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]
# print json.dumps(results[0]._json, indent=4)

# Get specific info isolated ino variables
status_texts = [ status._json['text'] for status in results ]

screen_names = [ status._json['user']['screen_name']
                            for status in results
                            for mention in status._json['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
                        for status in results
                        for hashtag in status._json['entities']['hashtags'] ]

words = [ word
            for text in status_texts
            for word in text.split() ]


# Figures out how many unique words 
# are in a list of text
def get_lexical_diversity(items):
    return 1.0*len(set(items))/len(items)

# Figures out the average number of words in a text
def get_average_words(tweets):
    total_words = sum([ len(tweet.split()) for tweet in tweets ])
    return 1.0*total_words/len(tweets)

print "Average words: %s" % get_average_words(status_texts)
print "Word Diversity: %s" % get_lexical_diversity(words)
print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
print "HashTag Diversity: %s" % get_lexical_diversity(hashtags)