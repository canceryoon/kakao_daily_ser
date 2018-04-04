import requests
import json
from bs4 import BeautifulSoup

def getCoinVal():
    return ({
            'message': {
                'text': '코인 종류를 선택하십시오'
             },
             'keyboard': {
                 'type': 'buttons',
                 'buttons' : ['BTC', 'ADA', 'SNT', 'ETH']
             }
           })

def getCoinUpbit():
    coinHdr = {'Content-Type': 'application/json; charset=utf-8', 'user-agent' : 'my-upbit-coin'}

    req = requests.get('https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.KRW-ADA&count=3&to=', headers=coinHdr).json()

    print(req)
    print(req[0])
    print(req[0]["tradePrice"])
    print(req[1]["tradePrice"])
    print(req[2]["tradePrice"])

#soup = BeautifulSoup(html, 'html.parser')
#print(soup)

