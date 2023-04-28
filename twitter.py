import tweepy
from textblob import TextBlob

# Authenticate with Twitter API
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Define search query and number of tweets to collect
query = 'Bitcoin'
num_tweets = 100

# Collect tweets
tweets = tweepy.Cursor(api.search_tweets, q=query, lang='en').items(num_tweets)

# Define function to perform sentiment analysis on a tweet
def get_tweet_sentiment(tweet_text):
    blob = TextBlob(tweet_text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'

# Analyze sentiments of collected tweets
positive_tweets = 0
negative_tweets = 0
neutral_tweets = 0

for tweet in tweets:
    tweet_text = tweet.text
    sentiment = get_tweet_sentiment(tweet_text)
    if sentiment == 'positive':
        positive_tweets += 1
    elif sentiment == 'negative':
        negative_tweets += 1
    else:
        neutral_tweets += 1

# Print sentiment analysis results
print(f"Out of {num_tweets} collected tweets on '{query}', the sentiment analysis is as follows:")
print(f"Positive tweets: {positive_tweets}")
print(f"Negative tweets: {negative_tweets}")
print(f"Neutral tweets: {neutral_tweets}")
