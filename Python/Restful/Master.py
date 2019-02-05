
# coding: utf-8

# Importing Necessary libraries

# In[1]:


import pandas as pd
from textblob import TextBlob

df = pd.read_csv('english_translated.csv')
cyc_df = pd.read_csv('cyclone.csv')
df.columns=['sno','tweet']
cyc_df['place']
# Finding the polarity and subjectivity of the tweet using sentiment analysis
# In[4]:
polarity = []
subjectivity = []

for tweet in df['tweet']:
    blob = TextBlob(tweet)
    po = polarity.append(blob.sentiment.polarity)
    su = subjectivity.append(blob.sentiment.subjectivity)

with open("sentimentt.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([po,su])