
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
    if addr[0][:2] == '서울' and len(addr) is not 3: 
        answer = "주소를 잘못 입력했습니다.\n\"서울 영등포구 여의도동\"\n 처럼 시,도 를 빼고 입력해주세요"
    else:
        wurl = 'https://api2.sktelecom.com/weather/current/hourly'
        wappKey = '4fb6735c-5fcc-4c33-82df-cc09d54d7088'
        wheaders = {'Content-Type': 'application/json; charset=utf8', 'appKey' : wappKey} 
        wjson = '' 

        if addr[0][:2] == '서울' :
            if addr[0][len(addr[0])-1] == '시':
                addr[0] = addr[0][:-1]

            wparams = { "version": "1", "city": addr[0], "county": addr[1], "village": addr[2]}
            wjson = requests.get(wurl, params=wparams, headers=wheaders).json()

            if 'error' in wjson: #not wjson["weather"] :
                answer = "주소를 잘못 입력했습니다.\n\"서울 영등포구 여의도동\"\n 처럼 시,도 를 빼고 입력해주세요"
            else:
                if not wjson["weather"]["hourly"] :
                       answer = "해당 주소에대한 날씨 정보가 없습니다.\n 잠시후에 다시 시도해주세요.";                                                
                else :
                    answer = "현재 기온 : " + str(wjson["weather"]["hourly"][0]["temperature"]["tc"]) + " ℃\n" \
                        + "풍속 : " + str(wjson["weather"]["hourly"][0]["wind"]["wspd"]) + " m/s\n" \
                        + "구름 : " + str(wjson["weather"]["hourly"][0]["sky"]["name"])

        else:
           gurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
           gparams = {"address" : addr, "key" : "AIzaSyAT_XkeGeEhvPIUYUVUDJElB0xpepmyfSM"} 
           gheaders =  {'Content-Type': 'application/json; charset=utf8'} 
           gjson =  requests.get(gurl, headers=gheaders, params=gparams).json()

           if not gjson["results"] :
               answer = "주소를 잘못 입력했습니다.\n\"서울 영등포구 여의도동\"\n 처럼 시,도 를 빼고 입력해주세요"
           else :
               lat = gjson["results"][0]["geometry"]["location"]["lat"]
               lng = gjson["results"][0]["geometry"]["location"]["lng"]
               lat = round(lat, 4)
               lng = round(lng, 4)

               wparams = { "version": "1", "lat": str(lat), "lon": str(lng)}
               wjson = requests.get(wurl, params=wparams, headers=wheaders).json()

               if 'error' in wjson:
                   answer = "주소를 잘못 입력했습니다.\n\"서울 영등포구 여의도동\"\n 처럼 시,도 를 빼고 입력해주세요"
               else :
                   if not wjson["weather"]["hourly"] :
                       answer = "해당 주소에대한 날씨 정보가 없습니다.\n 잠시후에 다시 시도해주세요.";                                                
                   else : 
                       answer = "현재 기온 : " + str(wjson["weather"]["hourly"][0]["temperature"]["tc"]) + " ℃\n" \
                           + "풍속 : " + str(wjson["weather"]["hourly"][0]["wind"]["wspd"]) + " m/s\n" \
                           + "구름 : " + str(wjson["weather"]["hourly"][0]["sky"]["name"])

    return { 'message': {
                'text': answer },
             'keyboard': {
                'type': 'buttons',
                'buttons' : ['날씨', '코인', '주식']
            }

           }
