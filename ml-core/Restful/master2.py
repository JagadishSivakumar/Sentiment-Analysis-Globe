#Master Python File This File Runs in the server
import re
import pandas as pd
from flask import Flask, jsonify, request
from flask_restful import Resource,Api
from google.cloud import translate
import time
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 

app = Flask(__name__)
api = Api(app)
app.secret_key ="A0Zr98j3yXRXHHjmNLWXRT"
key = app.secret_key

@app.route("/api/api", methods = ['GET'])
def getting():
    member = request.data
    print(member)
    return jsonify(member.decode("utf-8"))

@app.route("/api/multi12", methods = ['POST'])
def ETCL():
    df = pd.read_csv('cyclone.csv')
    head = df.head()
    tweets =head['tweet']
    result_tweet = []
    for tweet in head:
        text = tweet
        #removing links
        result = re.sub('http\S+','',text)
        result1 = re.sub('pic\S+','',result)
        #removing #
        result2 = re.sub('#\S+','',result)
        #removing @
        result3 = re.sub('@\S+','',result2)
        #removing emojis
        RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
        word = RE_EMOJI.sub(r'', result3)
            #appending in list
        result_tweet.append(word)
        # Converting into dictionary    
    d = {'tweet':result_tweet}
    csv_df = pd.DataFrame(d)
    csv_df.to_csv('cleaneddata.csv')
    return 201
@app.route("/api/wea")
def sentimentcleaner():
    f = pd.read_csv('english_translated.csv')
    cyc_df = pd.read_csv('cyclone.csv')
    df.columns=['sno','tweet']
    cyc_df['place']
    head = df.head()
    polarity = []
    subjectivity = []
    for tweet in head:
        blob = TextBlob(tweet)
        polarity.append(blob.sentiment.polarity)
        subjectivity.append(blob.sentiment.subjectivity)
    df['polarity'] = polarity
    df['subjectivity'] = subjectivity
    res_po = []
    res_sub = []
    res_tweet = []
    for index, row in df.iterrows():
        if (row['polarity'] != 0):
            res_po.append(row['polarity'])
            res_sub.append(row['subjectivity'])
            res_tweet.append(row['tweet'])
        dictio = {'tweet':res_tweet,'polarity':res_po,'subjectivity':res_sub}
    res_df = pd.DataFrame(dictio)
    head2 = res_df.head()       
    po = []
    twt = []
    sub = []
    for index, row in res_df.iterrows():
        a = (((row['polarity']+1)*4.5)-3)
        b = (((row['subjectivity']+1)*4.5)-3)
        c = row['tweet']
        po.append(round(a,4))
        sub.append(round(b,4))
        twt.append(c)
    final_dict = {'tweet':twt,'polarity':po,'subjectivity':sub}
    final_df = pd.DataFrame(final_dict)
    final_df.to_csv('senti_clean2.csv')
    return 200
         
        
@app.route("/api/multi21")
def translator():
    df = pd.read_csv('cleaned_data.csv')
    head = df.head()
    tweets = df['tweet']
    d = {}
    dlist = []
    translate_client = translate.Client()
    count = 0
    for tweet in tweets:
        result = translate_client.translate(tweet,target_language='en')
        count = count + 1
        dlist.append(result['translatedText'])
        if count == 500:
            count = 0
            time.sleep(240)
    csv_df = pd.DataFrame(dlist,columns=['tweet'])
    csv_df.to_csv('english_translated.csv')
    return 200

@app.route("/api/picword")
def cloud_generator():

    df = pd.read_csv(r"senti_clean2.csv", encoding ="latin-1") 
    comment_words = ' '
    stopwords = set(STOPWORDS) 
    header = df.head()
    for val in header:  
        val = str(val)
        tokens = val.split()
        for i in range(len(tokens)): 
            tokens[i] = tokens[i].lower()       
        for words in tokens: 
            comment_words = comment_words + words + ' '
    wordcloud = WordCloud(width = 800, 
                        height = 800, 
                        background_color ='white', 
                        stopwords = stopwords, 
                        min_font_size = 10).generate(comment_words)          
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.show()      
    return 200
       
# api.add_resource(hello,"/")
# api.add_resource(ETCL,"/api/etcl/")
# api.add_resource(sentimentcleaner,"/api/sEnTCl/")
# api.add_resource(translator,"/api/tRanSL")
# api.add_resource(cloud_generator,"/api/clDgen")

if __name__ == '__main__':
    app.run(port = 1337,debug=True)