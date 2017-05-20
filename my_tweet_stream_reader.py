import json
import pandas
import matplotlib.pyplot as plt
from collections import Counter
from prettytable import PrettyTable

tweets_data_path = 'my_tweet_mining.json'

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

print len(results) # print to test 

# create a dataframe
statuses = pandas.DataFrame()

# store the text values
statuses['text'] = map(lambda status: status['text'], results)
# store the language values
statuses['lang'] = map(lambda status: status['lang'], results)
# sometimes there may not be a place listed in the tweet
# so set to 'None' if not present
statuses['country'] = map(lambda status: status['place']['country']
                        if status['place'] != None else None, results)

statuses['retweet_count'] = map(lambda status: status['retweet_count'], results)



hashtags = [ hashtag['text']
            for status in results 
            for hashtag in status['entities']['hashtags'] ]

# get each tweet language and the count of its appearance
# (not to be confused with programming languages)
tweets_by_lang = statuses['lang'].value_counts() 
# get each tweet country of origin and the count of it's appearance
tweets_by_country = statuses['country'].value_counts()

retweet_count = statuses['retweet_count'].value_counts()
# create our drawing space/window(figure)
fig = plt.figure()

# prepare to plot two charts on the same figure
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

# style the axes and labels of our plot
ax1.tick_params(axis='x', labelsize=15)
ax1.tick_params(axis='y', labelsize=10)
ax1.set_xlabel('Number of retweets', fontsize=15)
ax1.set_ylabel('Number of tweets', fontsize=15)
ax1.xaxis.label.set_color('#666666')
ax1.yaxis.label.set_color('#666666')
ax1.tick_params(axis='x', colors='#666666')
ax1.tick_params(axis='y', colors='#666666')
# style the title
ax1.set_title('Retweet Count:', fontsize=15, color='#666666')

# plot the top 10 tweet languages and appearance count using a bar chart
retweet_count.plot(ax=ax1, kind='bar', color='#FF7A00')

# color the spines (borders)
for spine in ax1.spines.values():
    spine.set_edgecolor('#666666')

# second subplot
ax2.tick_params(axis='x', labelsize=15)
ax2.tick_params(axis='y', labelsize=10)
ax2.set_xlabel('Countries', fontsize=15)
ax2.set_ylabel('Number of tweets', fontsize=15)
ax2.xaxis.label.set_color('#666666')
ax2.yaxis.label.set_color('#666666')
ax2.tick_params(axis='x', colors='#666666')
ax2.tick_params(axis='y', colors='#666666')
# style the title
ax2.set_title('All Countries Tweeted From:', fontsize=15, color='#666666')

# plot the top 10 tweet languages and appearance count using a bar chart
tweets_by_country.plot(ax=ax2, kind='bar', color='#FF7A00')

# color the spines (borders)
for spine in ax2.spines.values():
    spine.set_edgecolor('#666666')

# render the graph
plt.show()







status_texts = [ status['text'] for status in results ]

screen_names = [ status['user']['screen_name']
                for status in results
                for mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
            for status in results 
            for hashtag in status['entities']['hashtags'] ]

words = [ w for t in status_texts
            for w in t.split() ]



for entry in [screen_names, hashtags, words]:
    counter = Counter(entry)
    print counter.most_common()[:10] # the top 10 results
    print

for label, data in (('Word', words), 
                    ('Screen Name', screen_names), 
                    ('Hashtag', hashtags)):
    pt = PrettyTable(field_names=[label, 'Count']) 
    c = Counter(data)
    [ pt.add_row(kv) for kv in c.most_common()[:10] ]
    pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
    print pt