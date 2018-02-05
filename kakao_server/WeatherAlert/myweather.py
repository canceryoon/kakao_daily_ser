
import requests
import json

def getaddr():
    return {
                'message': {
                    'text': '\"서울시 영등포구\" 형식으로 입력해주세요.'
                }
          }

def getweather(targetaddr):
    wurl = 'https://api2.sktelecom.com/weather/current/hourly'
    wappKey = '4fb6735c-5fcc-4c33-82df-cc09d54d7088'
    wheaders = {'Content-Type': 'application/json; charset=utf8', 'appKey' : wappKey} 
    wparams = { "version": "1", "city": "서울", "county": "영등포구", "village": "여의도동"}
    wjson = requests.get(wurl, params=wparams, headers=wheaders)
    print(wjson.json())

    return { 'message': {
                'text': wjson.json() }
           }
