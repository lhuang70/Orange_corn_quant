# General:
import tweepy
import time
import pandas as pd
import numpy as np
import re

from credentials import *    # import access key


def add_to_dataframe(data_frame, attr, tweets):
    data_frame[attr] = np.array([getattr(tweet, attr) for tweet in tweets])

def add_userdata_to_dataframe(data_frame, user, attri):
    temp = []
    for elements in user:
        temp.append(getattr(elements, attri))
    data_frame[attri] = np.array([tweet for tweet in temp])



def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

# API's setup:
def TwitterSetup():

    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


# creat an extractor object:
extractor = TwitterSetup()

words_extraction =["bitcoin"]
attribute_list = ["text","created_at", "id", "id_str", "source", "truncated",  "user", "coordinates", "place", "is_quote_status", "entities",  "favorited", "retweeted", "lang",  "retweet_count", "favorite_count"]
user_attribute_list = ["id", "id_str", "name", "screen_name", "location", "url", "description", "verified", "followers_count", "friends_count", "listed_count", "favourites_count", "statuses_count", "created_at", "utc_offset", "time_zone", "geo_enabled", "lang", "profile_image_url_https"]

combine_data = pd.DataFrame()

#number of extraction is 10, but can be change to a infinite while loop with sleep when actually extracting the data
for i in range(10):
    tweets = extractor.search(words_extraction[0], lang = 'en', count=200)
    data = pd.DataFrame(data=[clean_tweet(tweet.text) for tweet in tweets], columns=['Cleaned_Tweets'])

    #add all the attibuts to the dataframe
    for element in attribute_list:
        add_to_dataframe(data, element, tweets)

    for element in user_attribute_list:
        add_userdata_to_dataframe(data, data['user'], element)

    data["hash_tags"] = np.array([tweet['hashtags'] for tweet in data["entities"]])

    combine_data = combine_data.append(data, ignore_index=True)
    time.sleep(30)


combine_data.to_csv("bitcoin.csv", encoding='utf-8')
