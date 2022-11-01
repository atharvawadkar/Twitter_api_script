import tweepy
import configparser
import pandas as pd
#read 

config=configparser.ConfigParser()
config.read('config.ini')

api_key=config['twitter']['api_key']
api_key_secret=config['twitter']['api_key_secret']

access_token=config['twitter']['access_token']
access_token_secret=config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)

auth.set_access_token(access_token,access_token_secret)

api=  tweepy.API(auth)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

colums=['Time','User','Tweet']
Data=[]

for tweet in public_tweets:
    Data.append([tweet.created_at,tweet.user.screen_name,tweet.text])

df=pd.DataFrame(Data,columns=colums)
df.to_csv('tweets2.csv')