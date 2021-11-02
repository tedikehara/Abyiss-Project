

"""

    Theodore Ikehara 
    November 1, 2021
    Abyiss-Project

    Description: Monitors and updates the current status of select crypto exchanges in real time and displays to the browser.

"""

API_KEY = '''c1d3610a557a87beca88a20e781d37fa981a62c6658b46727b3cfe8a9c1927c9'''

import cryptocompare as cc
from selenium import webdriver

# crypto compare object
obj = cc.cryptocompare._set_api_key_parameter(API_KEY)
# selenium driver
location = "C:\Users\KShiro\Desktop\Abyiss-Project\Dependencies\chromedriver.exe"
driver = webdriver.Chrome(location)

driver.get("https://www.google.com")

# displays 10 crypto currencys and price in real time
while True:
    print('BTC PRICE: ', cc.get_price(['BTC', 'ETH', 'BNB', 'USDT', 'ADA', 'SOL', 'XRP', 'DOT', 'SHIB', 'DOGE'], currency='USD'))



