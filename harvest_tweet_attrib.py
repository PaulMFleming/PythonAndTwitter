import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'zIu1zNREssRYGougYYowx6FMR'
CONSUMER_SECRET = '5oGfKwcpw6z804ROBiuepycbj2Ks58G24LF7DnG4261YKptAVn'
OAUTH_TOKEN = '861653794618212353-AKK9BlHLBCcgO3Fg5pUrVLZ24g9XisN'
OAUTH_TOKEN_SECRET = 'wBickhWc05d1pMU8F49eImS9oEpKJvJHkjMuLxo4GlvXE'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 50
query = 'Dublin'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [ status._json['text'] for status in results ]

screen_names = [ status._json['user']['screen_name']
                                for status in results
                                        for mention in status._json['entities']['user_mentions']]

hashtags = [ hashtag['text']
                        for status in results
                            for hashtag in status._json['entities']['hashtags']]

words = [ words
                        for text in status_texts
                            for word in text.split() ]

print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1)
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)