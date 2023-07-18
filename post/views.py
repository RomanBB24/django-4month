from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello its my first project")


def now_date(request):
    if request.method == 'GET':
        now_time = datetime.now()
        return HttpResponse(now_time)


def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodby user")
