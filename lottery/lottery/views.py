import random
from django.shortcuts import render

def lottery_index(request):
    return render(request, 'index.html')

def lottery_result(request):
    try:
        game_count = int(request.GET.get('game_count'))
    except:
        game_count = 0
    return render(
        request,
        'result.html',
        {'results': [random.sample(range(1, 46), 7) for _ in range(game_count)]}
    )
