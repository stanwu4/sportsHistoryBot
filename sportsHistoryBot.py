from bs4 import BeautifulSoup
import os
import re
from datetime import datetime  # Used for getting current date
import requests
import time
import tweepy  # Twitter API
import random

import realAuthentication
# Holds twitter login data.

api = realAuthentication
#returns api object from website and twitter

#steps to code
#intialize the method at the time of the hour, which would be noon 12:00 pm
#at that time, you can intialize the method, which goes onto statmuse and grabs the statistic of the day with beautiful soup
#then open twitter and create a tweet, copy pasting the stat into the tweet, maybe search up an image of the player on google
#finally publish the tweet
#problems: how to fit into 280 characters if the statmuse sentence is longer than that
class Stats
    def grabStats(string s):
        
    def tweetOut(string s):
        api.updateStatus(s)
    def main():
        time = datetime.datetime.now()
        string tweet = ""
        if(time.strftime("%I:%M:%S %p") == "12:00:00 AM"){
            grabStats(tweet)
            tweetOut(tweet)
        }