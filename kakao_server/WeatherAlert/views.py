from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from django.http import JsonResponse

import json
import sys
sys.path.insert(0, '/home/ubuntu/kakao_server/WeatherAlert')

import myweather

def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons' : ['날씨', '코인', '주식']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    var_keyboard = received_json_data['content']

    if var_keyboard == '날씨':
        return JsonResponse(myweather.getaddr())
    elif var_keyboard == '코인':
        print('코인')
    elif var_keyboard == '주식':
        print('주식')
    else:
        return JsonResponse(myweather.getweather(var_keyboard))

    return JsonResponse({
            'message': {
                'text': var_keyboard + ' 선택했습니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons' : ['날씨', '코인', '주식']
            }

        })
