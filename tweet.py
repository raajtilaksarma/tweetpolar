import tweepy
import pandas as pd
from tweepy import OAuthHandler
from textblob import TextBlob

class Tweety():
    def __init__(self, ):
        # consumer_key= 'CONSUMER_KEY_HERE'
        # consumer_secret= 'CONSUMER_SECRET_HERE'
        # access_token='ACCESS_TOKEN_HERE'
        # access_token_secret='ACCESS_TOKEN_SECRET_HERE'
        # authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
            self.tweet_count = 1000 
        except:
            print("Error: Authentication Failed")
            
    def getTweets(self, word):
        self.public_tweets = self.api.search(word,count = self.tweet_count,tweet_mode='extended')

    def polarizedTweets(self):
        list_tweet = []
        list_pol = []
        for tweet in self.public_tweets:
            tweet_text = tweet.full_text
            analysis = TextBlob(tweet_text)
            tweet_polarity = abs(analysis.sentiment.polarity)
            list_tweet.append(tweet_text)
            list_pol.append(tweet_polarity)
        df = pd.DataFrame({'tweet':list_tweet, 'polarity':list_pol},columns=['tweet','polarity'])
        df.sort_values(by=['polarity'],ascending=False,inplace=True)
        df = df[:10]
        self.polarized_tweets = df['tweet'].unique().tolist()
        return self.polarized_tweets