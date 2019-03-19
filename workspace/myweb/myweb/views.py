from django.shortcuts import HttpResponse
from django.shortcuts import render

def index(request) :
    '''
    settings.py의 INSTALLED_APPS에서 myweb 폴더 추가. templates에 있는 html 문서를 render()로 출력
    '''
    return render(request, 'index.html')

def blog(request) :
    return render(request, 'blog.html')

def html(request) :
    return render(request, 'html.html')

def css(request) :
    return render(request, 'css.html')

def js(request) :
    return render(request, 'js.html')


