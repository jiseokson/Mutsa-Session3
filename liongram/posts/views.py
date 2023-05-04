from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def url_view(request):
    return HttpResponse('<h1>url view</h1>')
    # return JsonResponse({'name': 'Jiseok'})

def url_parameter_view(request, username):
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')
