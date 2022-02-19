from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse('\r\nHello World')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
