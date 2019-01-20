import pandas as pd 
import csv
sno = []
data = pd.read_csv("cyclone.csv")
tweets = data["tweet"]
with open("only_tweets.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([sno,tweets])
#from googletrans import Translator
#translator = Translator()