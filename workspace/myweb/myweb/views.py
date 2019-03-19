from django.shortcuts import HttpResponse
from django.shortcuts import render

def index(request) :
    '''
    settings.py의 INSTALLED_APPS에서 myweb 폴더 추가. templates에 있는 html 문서를 render()로 출력
    '''
    return render(request, 'index.html')

def blog(request) :
    return HttpResponse('Blog')

def html(request) :
    return HttpResponse('HTML Page')

def css(request) :
    return HttpResponse('CSS Page')

def js(request) :
    return HttpResponse('JavaScript Page')


