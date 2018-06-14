from flask import Flask
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    r = {"MSG" : "HELLO WORLD!"}
    return json.dumps(r)

@app.route("/submitToTheVoid/<summoner_name>",methods=['GET'])
def submitToTheVoid(summoner_name):
    apiKey = "RGAPI-23e2ed89-05c6-4eca-8aeb-d97c9e658d4e"
    response = requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+summoner_name+"?api_key="+apiKey)
    response2 = requests.get("https://nal.api.riotgames.com/lol/match/v3/matchlists/by-account/"+response[id]+"?api_key="+apiKey)
    return response.text +"\n " +response2.text +"\n "+ apiKey
    
