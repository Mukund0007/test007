from flask import Flask, render_template,request,jsonify
import requests
#import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
	
@app.route("/get")
def getBotResponse():
    query = request.args.get('msg')
    #response = requests.get("http://localhost:5000/parse",params={"q":query})
    #response = response.json()
    #topresponse = response["topScoringIntent"]
    #intent = topresponse.get("intent")
    #return str(intent)
    if query == "4tech":
        response_text = "http://4technologies.in/"
    else:
        response_text = query
    return str(response_text)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port = 80)
    
