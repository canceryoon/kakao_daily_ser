
import requests
import json

def getaddr():
    return {
                'message': {
                    'text': '\"서울 영등포구 여의도동\" 형식으로 입력해주세요.'
                }
          }

def getweather(targetaddr):
    addr = targetaddr.split()

    if len(addr) is not 3: 
        answer = "주소를 잘못 입력했습니다.\n\"서울 영등포구 여의도동\"\n 처럼 시,도 를 빼고 입력해주세요"
    else:
        wurl = 'https://api2.sktelecom.com/weather/current/hourly'
        wappKey = '4fb6735c-5fcc-4c33-82df-cc09d54d7088'
        wheaders = {'Content-Type': 'application/json; charset=utf8', 'appKey' : wappKey} 
        wparams = { "version": "1", "city": addr[0], "county": addr[1], "village": addr[2]}
        wjson = requests.get(wurl, params=wparams, headers=wheaders).json()

        if not wjson["weather"]["hourly"] :
            answer = "주소를 잘못 입력했습니다.\n\"서울 영등포구 여의도동\"\n 처럼 시,도 를 빼고 입력해주세요"
        else:
            answer = "현재 기온 : " + str(wjson["weather"]["hourly"][0]["temperature"]["tc"]) + " ℃\n" \
                + "풍속 : " + str(wjson["weather"]["hourly"][0]["wind"]["wspd"]) + " m/s\n" \
                + "구름 : " + str(wjson["weather"]["hourly"][0]["sky"]["name"])
    print(answer)
    print(targetaddr)

    return { 'message': {
                'text': answer },
             'keyboard': {
                'type': 'buttons',
                'buttons' : ['날씨', '코인', '주식']
            }

           }
