# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:37:32 2015

@author: andrew
"""

import pandas as pd

tweetfile = 'tweets.csv'
tweets = pd.read_csv(tweetfile,delimiter='\t')
tweets['timestamp'] = [pd.to_datetime(t,unit='s') for t in tweets.tweettime]
tweets.index = tweets['timestamp']
tweets = tweets.drop(['tweettime'],axis=1)
tweets_unique = tweets.drop_duplicates(subset='tweetid')
tweets_unique = tweets_unique.sort('tweetid')

incidentfile = 'incidents.csv'
incidents = pd.read_csv(incidentfile)
incidents.index = incidents['timestamp']
incidents = incidents.sort('timestamp')

# set up 10 minute time slices, record len(tweets_subset) and
# len(incidents_subset) for each
p = pd.date_range(tweets_unique.timestamp[0],tweets_unique.timestamp[-1],freq='10t')
numTweets = []
numIncidents = []
for i in range(1,len(p)):
    numTweets.append(len(tweets_unique[str(p[i-1]):str(p[i])]))
    numIncidents.append(len(incidents[str(p[i-1]):str(p[i])]))

df_dict = {'numTweets' : numTweets, 'numIncidents' : numIncidents}
df = pd.DataFrame(df_dict)
df.index = p[0:-1]
df.plot(y=['numIncidents','numTweets'])