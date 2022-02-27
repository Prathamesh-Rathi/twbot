import tweepy
import time

consumer_key='Your consumer key'
consumer_secret='your consumer secret'
access_token='Your acess token'
access_token_secret ='Your acess token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

FILE_NAME = 'IdStorage.txt'

def read_Last_seen(FILE_NAME):
    file_read = open(FILE_NAME , 'r')
    Last_seen_id = int(file_read.read().strip())
    file_read.close()
    return Last_seen_id

def store_last_seen(FILE_NAME , Last_seen_id):
    file_write = open(FILE_NAME,'w')
    file_write.write(str(Last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(since_id=read_Last_seen(FILE_NAME), tweet_mode = 'extended')
    for tweet in reversed(tweets):
        if '#learnpython' in tweet.full_text.lower():
            print("Replied to ID -" + str(tweet.id))
            api.update_status("@"+ tweet.user.screen_name + "keep learning", tweet.id )
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME,tweet.id)

while True:
    reply()
    time.sleep(15)