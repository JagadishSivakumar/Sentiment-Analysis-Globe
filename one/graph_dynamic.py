import json
import requests
from flask import Flask, abort, jsonify, request

app = Flask(__name__)

@app.route("/graphero", methods = ['POST'])
def graphero():
	data =  {
  				type: 'line',
  				data: {
    					labels: [14,15,16,17,18,19,20,21,22,23,24],
    					datasets: [{ 
        						data: [98,150,188,250,480,520,690,820,710,380,460],
        						label: "Food",
        						borderColor: "#3e95cd",
        						fill: false
      					}, { 
        						data: [48,58,98,100,210,130,100,185,175,165,135],
        						label: "Clothes",
        						borderColor: "#8e5ea2",
        						fill: false
      					}, { 
        						data: [148,215,198,250,330,186,218,172,167,177,164],
        						label: "Shelter",
        						borderColor: "#3cba9f",
        						fill: false
      					}, { 
        						data: [115,195,320,410,440,520,360,360,284,210,150],
        						label: "Health Emergency",
        						borderColor: "#e8c3b9",
        						fill: false
      						}, 
    						]
  							},
  							options: {
    							title: {
      									display: true,
      									text: 'Contributions through Lexicon'
    									}
  									}
			}

	url = "http://127.0.0.1:9000/graphero"

	r = requests.post(url,data)
	print(str(r.content, 'utf-8'))
if (__name__ == "__main__"):
	app.run(port = 9000, debug = True)

