import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    api_key = "240aa650f4db4e154a07d0459c30a347"
    lat = "39.571625"
    lon = "2.650544"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)


app.run(port=8080)