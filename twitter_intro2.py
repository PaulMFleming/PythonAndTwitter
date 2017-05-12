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

DUB_WOE_ID = 560743

dub_trends = api.trends_place(DUB_WOE_ID)

print json.dumps(dub_trends, indent=1)
