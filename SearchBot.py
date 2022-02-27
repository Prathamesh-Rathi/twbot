import tweepy
import time


consumer_key='Your consumer key'
consumer_secret='your consumer secret'
access_token='Your acess token'
access_token_secret ='Your acess token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

hashtag = "100daysofcode"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
            

        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)


def likebot():
    for tweet in tweets:
        try:
            tweet.create_favorite()
            print("like Done!")
            time.sleep(2)
            

        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)
searchbot()
likebot()