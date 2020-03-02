from django.http import JsonResponse
from django.shortcuts import render
import time,json
# Create your views here.
from django.utils.safestring import mark_safe
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



def aaa(request):
    return render(request,'chat.html')


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def pushRedis(request):
    room = request.GET.get('room')


    def push(msg):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            room,
            {
                "type": "tui.song",
                'msg':msg
            }
        )

    push('推送测试！')
    return JsonResponse({'1':1})
