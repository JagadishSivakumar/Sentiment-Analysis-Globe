# Sentiment Globe Data

## Globe Plotting data - 

### Original Globe plotting data
var data = [ 

['A Series',[lattitude,longitude,magnitude,lattitude,longiude,magnitude,....]] , 

['B Series',[lattitude,longitude,magnitude,lattitude,longiude,magnitude,....]] ,

['C Series',[lattitude,longitude,magnitude,lattitude,longiude,magnitude,....]],

];

Series => Each Strip on Globe

### Our Required Json 
[ ' no.lines ' ,[ [lattitude,longitude,magnitude,lattitude,longiude,magnitude,....]] ,
' no.lines ' ,[ [lattitude,longitude,magnitude,lattitude,longiude,magnitude,....]] ,
]

## Cyclone.csv 
[ ID, convId, date , time , user id, user_name , user full name , tweet, pic, pic link, retweet count,likes,hashtag,quotes,...]

## cleaned_data.csv
[S.no,tweet]
Contains the tweets of cyclone.csv in cleaned manner by removing links, hashtags, Tags and emojis

## only_tweets.csv
[Sno,tweet]
          *the tweets can be in regional language*
          
## Translated.csv          
[Sno,tweet]
           *tweets are only in english*
           *the entire set of tweets are present in a single dataframe*
# Sample UI
Checkout the UI & UX readme
