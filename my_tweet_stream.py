from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from settings import twitter_app_config

CONSUMER_KEY = twitter_app_config.get('CONSUMER_KEY')
CONSUMER_SECRET = twitter_app_config.get('CONSUMER_SECRET')
OAUTH_TOKEN = twitter_app_config.get('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = twitter_app_config.get('OAUTH_TOKEN_SECRET')

# list of strings to search for
keyword_list = ['trumpimpeachment','globalseedbank','americangods','guardiansofthegalaxy2']

# customize the class here
class MyStreamListener(StreamListener):

    def on_data(self, data): 
        try:
            with open('my_tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True

    def on_error(self, status):
        print status
        return True

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)