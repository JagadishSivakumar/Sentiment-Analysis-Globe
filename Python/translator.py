from googletrans import Translator
import csv
import pandas as pd

data = pd.read_csv("only_tweets.csv")
translator = Translator()
'''text = 
for i in data[2]:
        translated = translator.traslate(i)
print(translated)        
'''


'''
translator = Translator()
ta_text = "திருவாரூர் மக்கள் இடைத் தேர்தலை விரும்பவில்லை - ஜெயகுமார். அடேய் இதுவும் அம்மா இட்டிலி சாப்பிட்ட கதை தான் டா!"
conf = translator.detect(ta_text)
print(conf)
en_text = translator.translate(ta_text)
print(en_text)
'''


sno = []
data = pd.read_csv("only_tweets.csv")
gs = goslate.Goslate()
for i in data:
        text = gs.translate(i,"en")
with open("Translated.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([sno,text])

       
