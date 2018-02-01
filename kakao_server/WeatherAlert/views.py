from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from django.http import JsonResponse
import json

def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons' : ['날씨', '코인', '주식']
    })

@csrf_exempt
def answer(request):
    print("In anser");
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    cafeteria_name = received_json_data['content']
    return JsonResponse({
            'message': {
                'text': cafeteria_name + ' 선택했습니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons' : ['날씨', '코인', '주식']
            }

        })
