import tweepy
import time
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.key, config.secret)
api = tweepy.API(auth)

FILE_NAME = 'log.txt'

def read_log(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    log_id = int(file_read.read().strip())
    file_read.close()
    return log_id

def store_log(FILE_NAME, log_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(log_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_log(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#Cityzens開発記録' in tweet.full_text:
            print("Reply to twId - " + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + "進捗はドウダネ？マダマダネレナイネ！俺ケビンデブライネ", tweet.id)
            api.create_favorite(tweet.id)
            store_log(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)
    print("Working...")