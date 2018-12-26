import tweepy
from tweepy import OAuthHandler
import requests
import json

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def getTweet(keyword,api):
    for tweet in tweepy.Cursor(api.search,
                               q=keyword,
                               rpp=100,
                               result_type="recent",
                               include_entities=True,
                               lang="tr").items():
        name = tweet.user.name
        text = tweet.text
        time = tweet.created_at
        rating = (2*tweet.retweet_count)+ tweet.favorite_count
        out =  name +","+text+","+ str(time) + ","+ str(rating)
        out = out.encode('utf-8')
        print out

        with open('tweet.txt', 'a') as f:
            f.write(out)

getTweet("keyword",api)
