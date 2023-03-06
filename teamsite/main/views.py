from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseNotAllowed


def index(request):
    return render(request, 'main/main_page.html')


def info(request):
    return render(request, 'main/info.html')


def buy(request):
    return render(request, 'main/buy.html')


def buy2(request):
    return render(request, 'main/buy2.html')


def sub(request):
    return render(request, 'main/subscribe.html')


def prod(request):
    return render(request, 'main/prod.html')


def prod2(request):
    return render(request, 'main/prod2.html')


def prod3(request):
    return render(request, 'main/prod3.html')





