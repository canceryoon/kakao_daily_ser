import requests
import json
from bs4 import BeautifulSoup

def getCoinVal():
    return ({
            'message': {
                'text': 'Choose a coin type.'
             },
             'keyboard': {
                 'type': 'buttons',
                 'buttons' : ['BTC', 'BCC', 'ETH', 'DASH', 'ZEC', 'XMR', 'LTC', 'NEO', 'BTG', 'REP', 'ETC', 'QTUM', 'OMG', 'LSK', 'EOS', 'PIVX', 'STRAT', 'WAVES', 'MTL', 'KMD', 'ARK', 'ICX', 'VTC', 'SBD', 'STEEM', 'STORJ', 'GRS', 'XRP', 'TIX', 'POWR', 'ARDR', 'XEM', 'XLM', 'MER', 'EMC2', 'ADA', 'SNT', 'TRX', 'STORM']

             }
           })

def getCoinUpbit(coin):
    coinHdr = {'Content-Type': 'application/json; charset=utf-8', 'user-agent' : 'my-upbit-coin'}
    coinUrl = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.KRW-' + coin +'&count=1&to='
    req = requests.get(coinUrl, headers=coinHdr).json()
    tradeT = req[0]["candleDateTimeKst"]
    tradeDate = tradeT.split('T', 1)[0]
    tradeTime = tradeT.split('T', 1)[1][:5]
    
    tPrice = str(req[0]["tradePrice"])
    hPrice = str(req[0]["highPrice"])
    lPrice = str(req[0]["lowPrice"])

    return ( 'Trading Time: \n' + tradeDate + ' ' + tradeTime + '\n' + coin + ' High Price: ' +  hPrice + 'won\n' + coin + ' Low Price: ' + lPrice + 'won\n' + coin + ' Price: ' + tPrice + 'won')
