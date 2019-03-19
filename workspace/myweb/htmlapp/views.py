from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request) :
    return render(request, 'html/index.html')

def html2(request) :
    return render(request, 'html/html2.html')