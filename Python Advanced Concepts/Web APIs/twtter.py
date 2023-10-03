import tweepy

key = "{{rJFfShlQS4bvFNCgzMt9KQT7v}}"
secret = "{{WwmXNZiiN2SGH8HYkMQpCLIDsAX7UnE95GuHqznCIav6My6QZi}}"
access_token = "{{1547333848064790531-J88XGTrnxR9ONieELryNpTclaAtJ1E}}"
access_secret = "{{RaYOYQTGDEQR9poLmMnqcyVkbeupddaxtyAhbz5k3iqMq}}"
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

my_tweets = api.user_timeline()

for tweet in my_tweets:
    print(tweet.text)