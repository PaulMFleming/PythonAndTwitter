import json
import pandas
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'

# loop through the JSON file line by line and add 
# tweets to the results list
results = [] 
tweets_file = open(tweets_data_path, 'r')
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue
        
print len(results)