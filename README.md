# Sentiment Globe Data

# Sample UI
Checkout the UI & UX readme

## Globe Plotting data - 

### Original Globe plotting data
var data = [ 

['A Series',[lattitude,longitude,magnitude,lattitude,longiude,magnitude,....]] , 

['B Series',[lattitude,longitude,magnitude,lattitude,longiude,magnitude,....]] ,

['C Series',[lattitude,longitude,magnitude,lattitude,longiude,magnitude,....]],

];

Series => Each Strip on Globe

### Required Json 
[ ' no.lines ' ,[ [lattitude,longitude,magnitude,lattitude,longiude,magnitude,....]] ,
' no.lines ' ,[ [lattitude,longitude,magnitude,lattitude,longiude,magnitude,....]] ,
]

# Python and Backend

## Data Files

### Cyclone.csv 
[ ID, convId, date , time , user id, user_name , user full name , tweet, pic, pic link, retweet count,likes,hashtag,quotes,...]

### cleaned_data.csv
[S.no,tweet]
Contains the tweets of cyclone.csv in cleaned manner by removing links, hashtags, Tags and emojis

### only_tweets.csv
[Sno,tweet]
          *the tweets can be in regional language*
          
### Translated.csv          
[Sno,tweet]
           *tweets are only in english*
           *the entire set of tweets are present in a single dataframe*

## Notebook Files

# ECTL.ipynb
Performs translation and cleaning process of removing links, hashtags, tags and emojis and store only the cleaned tweets in another file.
Input File is *cyclone.csv*
Output File is *cleaned_data.csv*

