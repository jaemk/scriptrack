from django.shortcuts import render

from django.http import HttpResponse as httpresp

def index(request):
    return render(request, 'main/index.html')
    #return httpresp('Welcome to main page index')
