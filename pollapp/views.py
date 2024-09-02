from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("First Poll App!")

def index2(request):
    return HttpResponse("First Poll App Views/urlsTest!")