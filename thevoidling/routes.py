from flask import Flask
from flask import request
from flask_cors import CORS
from thevoidling import app,db


import requests
import json
import sys


apiKey = ""


@app.route("/")
def hello():
    r = {"MSG" : "Math WORLD!"}

    return json.dumps(r)

@app.route("/submitToTheVoid/<summoner_name>",methods=['GET'])
def submitToTheVoid(summoner_name):
    response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summoner_name+"?api_key="+apiKey)
    r = response.json()
    print(r)
    response = requests.get("https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+str(r['id'])+"?api_key="+apiKey)
    return response.text
    
@app.route("/matchList/<summoner_name>",methods=['GET'])
def matchList(summoner_name):
    response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summoner_name+"?api_key="+apiKey)
    r = response.json()
    response = requests.get("https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+str(r['accountId'])+"?api_key="+apiKey)

    return response.text

@app.route("/activeGame/<account_id>",methods=['GET'])
def activeGame(account_id):
    response = requests.get("https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+account_id+"?api_key="+apiKey)
    return response.text

@app.route("/getChamp/",methods=['GET'])
def matchTimeline():
    response = requests.get("https://na1.api.riotgames.com/lol/static-data/v4/champions/?api_key="+apiKey)
    return response.text

@app.route("/gatherData/",methods=['GET'])
def gatherData():
    return 0

@app.route("/hextechUltimatum/",methods=['GET'])
def oneVOne():
    p1 = {}
    p2 = {}
    p1['sumName'] = request.args.get('p1SumName')
    p2['sumName'] = request.args.get('p2SumName')
    p1['champName'] = request.args.get('p1CName')
    p2['champName'] = request.args.get('p2CName')
    
    champListRes = requests.get("https://na1.api.riotgames.com/lol/static-data/v4/champions/?api_key="+apiKey)
    champList = champListRes.json()['data']
    
    p1ChampID = champList[p1['champName']]['id']
    p2ChampID = champList[p2['champName']]['id']

    p1Data = getPlayerRankData(p1['sumName'],p1ChampID)
    p1Data['champName'] = p1['champName']
    p2Data = getPlayerRankData(p2['sumName'],p2ChampID)
    p2Data['champName'] = p2['champName']   
    
    
    return json.dumps([p1Data,p2Data])
    

romantoInt = {
    'I'  : 1,
    'II' : 2,
    'III': 3,
    'IV' : 4,
    'V'  : 5
}

hackELO = {
    'BRONZE': [800,1149],
    'SILVER': [1150,1499],
    'GOLD'  : [1500,1849],
    'PLATINUM':[1850,2199],
    'DIAMOND': [2200,2599],
    'MASTER' : 2600,
    'CHALLENGER': 2600
}

def getPlayerRankData(sumName,champID):
    response = {}
    sum = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+sumName+"?api_key="+apiKey).json()
    sumRankRes = requests.get("https://na1.api.riotgames.com/lol/league/v4/positions/by-summoner/"+str(sum['id'])+"?api_key="+apiKey)
    sumRank = sumRankRes.json()

    maxElo = hackELO[sumRank[0]['tier']][1]
    minElo = hackELO[sumRank[0]['tier']][0]
    division = romantoInt[sumRank[0]['rank']]

    response['ELO'] = (((maxElo - minElo)/5) * (5.5 - division)) + minElo
    mast = requests.get("https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+str(sum['id'])+"/by-champion/"+str(champID)+"?api_key="+apiKey).json()
    
    response['championPoints'] = mast['championPoints']
    response['sumName'] = sumName
    return response