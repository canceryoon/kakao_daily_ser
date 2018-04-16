from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from django.http import JsonResponse

import json
import sys
sys.path.insert(0, '/home/ubuntu/kakao_server/WeatherAlert')

import myweather
import mycoin
import mybestsellers

def webhome(request):
    return render(request, 'webpage/home.html', {})

def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons' : ['Weather', 'Coin', 'Books']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    var_keyboard = received_json_data['content']

    bookList = ["신간", "주목할 만한 신간", "베스트셀러"]
    answer = ''

    if len(var_keyboard) is 3 :
        answer = mycoin.getCoinUpbit(var_keyboard);

    elif var_keyboard == 'Weather':
        return JsonResponse(myweather.getaddr())

    elif var_keyboard == 'Coin':
        return JsonResponse(mycoin.getCoinVal())

    elif var_keyboard == 'Books':
        return JsonResponse(mybestsellers.getListType())

    elif var_keyboard in bookList:
        answer = mybestsellers.getBestSellers(var_keyboard)

    elif answer == '':
        answer = myweather.getweather(var_keyboard)

    return JsonResponse({
            'message': {
                'text': answer
            },
            'keyboard': {
                'type': 'buttons',
                'buttons' : ['Weather', 'Coin', 'Books']
            }

        })
