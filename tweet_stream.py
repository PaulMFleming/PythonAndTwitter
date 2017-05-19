from tweepy import Stream # connects to Twitter stream (live tweets)
from tweepy import OAuthHandler 
from tweepy.streaming import StreamListener # pulls in the stream data
from settings import twitter_app_config

CONSUMER_KEY = twitter_app_config.get('CONSUMER_KEY')
CONSUMER_SECRET = twitter_app_config.get('CONSUMER_SECRET')
OAUTH_TOKEN = twitter_app_config.get('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = twitter_app_config.get('OUATH_TOKEN_SECRET')

# list of strings to search for (good idea: search for what's trending atm)
keyword_list = ['WonderWoman','IrishFilm','Cannes2017','Syria'] # track list

# this is an extension to the StreamListener class we imported
# we need to extend the class in order to customize the incoming data
# to suit our needs
class MyStreamListener(StreamListener):

    def on_data(self, data): # override the StreamListener on_data() function
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True

    def on_error(self, status): # override the Stream_Listener on_error() function
        print status
        return True

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# create an instance of the stream and pull in
# the data by filtering for our ketwords
twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list) 
        