import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "@Aspirin_4140"
tweet_list = []  

for tweet in sntwitter.TwitterSearchScraper(query).get_items(): 
		tweet_list.append([tweet.date, tweet.user.username, tweet.user.displayname, tweet.content, tweet.url])
		
		 
df = pd.DataFrame(tweet_list, columns = ['Date', 'User', 'Nickname', 'Tweet', 'URL'])

print(df) 
