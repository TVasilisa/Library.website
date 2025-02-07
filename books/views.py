from datetime import datetime

from django.http import HttpResponse


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовет Василиса, учусь на направлении Backend')


def text_and_photo(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://cs6.pikabu.ru/post_img/2014/05/15/10/1400167833_1703122734.jpg"/>')


def system_time(request):
    if request.method == 'GET':
        current_time = datetime.today()
        return HttpResponse(current_time)
