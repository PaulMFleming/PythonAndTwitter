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

count = 10
query = 'Dublin'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]
print json.dumps(results[0]._json, indent=4)

for status in results:
    print status.text.encode('utf-8')
    print status.user.id
    print status.user.screen_name
    print status.user.profile_img_url_https
    print status.user.followers_count
    print status.place