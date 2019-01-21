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

## only_tweets.csv
[Sno,tweet]
          *the tweets can be in regional language*
          
## Translated.csv          
[Sno,tweet]
           *tweets are only in english*
           *the entire set of tweets are present in a single dataframe*
# Sample UI
![screenshot 2019-01-21 at 7 38 21 pm](https://user-images.githubusercontent.com/27012182/51481513-0b2afd00-1dba-11e9-95a9-35ef24d15566.png)
