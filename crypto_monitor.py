

"""

    Theodore Ikehara 
    November 1, 2021
    Abyiss-Project

    Description: Monitors and updates the current status of select crypto exchanges in real time and displays to the browser.

"""

from flask import Flask
import cryptocompare as cc
from datetime import date
from datetime import datetime

API_KEY = '''c1d3610a557a87beca88a20e781d37fa981a62c6658b46727b3cfe8a9c1927c9'''
# crypto compare object
obj = cc.cryptocompare._set_api_key_parameter(API_KEY)

app = Flask(__name__)

@app.route("/")
def monitor():
    return "{} {} {} {} {}".format(date.today(), ',',datetime.now().strftime("%H:%M:%S"), ',:',cc.get_price(['BTC', 'ETH', 'BNB', 'USDT', 'ADA', 'SOL', 'XRP', 'DOT', 'SHIB', 'DOGE'], currency='USD'))


if __name__ == "__main__":
        app.run()





