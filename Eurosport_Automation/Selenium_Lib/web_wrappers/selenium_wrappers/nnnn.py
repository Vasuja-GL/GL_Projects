import csv
import tweepy as tw
import pandas as pd
# Variables that contains the user credentials to access Twitter API
access_token = '1440466843-ZUV0vsslINHTx4rLiuAcMM9MWr8RFgy82n0f26i'
access_token_secret = 'QeniIW83vY1OuYufwQa1PWHed7BzreC5VfDATKDvQbHmr'
consumer_key = '0pT8lSkWUjuMflnMWv1LU9McE'
consumer_secret = 'blOfzyOOZLj7uIaZXMNKLhnDzO3EAbY5VB94MbaoLQvD0sk8mE'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('maha.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tw.Cursor(api.search,q="#MaharashtraGovtFormation",count=100,lang="en",since="2019-11-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])