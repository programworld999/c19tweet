import tweepy
import requests
from bs4 import BeautifulSoup
import json

twitterAPIKey = json.load(open("./twitter-api-key.json", "r"))
consumer_key = twitterAPIKey['consumer_key']
consumer_secret = twitterAPIKey['consumer_secret']
access_token = twitterAPIKey['access_token']
access_token_secret = twitterAPIKey['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def Tweet(content):
    api.update_status(status=content)
    print("Tweeted")

    # tweetData = r"Covid19India Update "+content["date"]+" \n    Total:\n        Confirmed: "+content["totalconfirmed"]+"\n        Active: "+str(int(content["totalconfirmed"])-int(content["totalrecovered"])-int(content["totaldeceased"]))+"\n        Recovered: "+content["totalrecovered"]+"\n        Death: "+content["totaldeceased"]+"\n    Daily Data:\n        Confirm: "+content["dailyconfirmed"]+"\n        Recovered: "+content["dailyrecovered"]+"\n        Death: "+content["dailydeceased"]+"\n#COVID19 #IndiaFightsCorona"
