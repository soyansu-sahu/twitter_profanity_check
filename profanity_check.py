import pandas as pd

slurs_df = pd.read_csv('profane_words.csv', encoding='latin1')
tweets_df = pd.read_csv('train.csv')
tweets = tweets_df.tweet.tolist()

def get_degree_of_profanity(tweet):
    """
    Function to get profanity of a tweet given a list of slurs.
    Args:
        tweet(str): Tweet string to be analysed.
    Return:
        Profanity(int)
    """
    words_in_tweet = tweet.split(' ')
    slur_ratings = slurs_df.loc[slurs_df.english.isin(words_in_tweet),'rating']
    profanity = slur_ratings.sum()
    return profanity

def find_profanities(tweets):
    """
    Function to get profanity of a a list of tweets.
    Args:
        tweets(list): Tweets to be analysed.    
    """
    profanities = [get_degree_of_profanity(tweet) for tweet in tweets]
    output_df = pd.DataFrame({"tweet": tweets, "profanity":profanities})
    output_df.to_csv("profanities_df.csv", index=False)

    return

if __name__=='__main__':
    find_profanities(tweets)