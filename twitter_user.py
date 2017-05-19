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

user = api.get_user('@neilhimself')

print user.screen_name
print user.followers_count

for friend in user.friends():
    print
    print friend.screen_name
    print friend.followers_count