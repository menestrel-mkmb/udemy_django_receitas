from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('\r\nHello World')

def about(request):
    return HttpResponse('\r\nHello About')

def contact(request):
    return HttpResponse('\r\nHello Contact')
