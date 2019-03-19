from django.shortcuts import HttpResponse

def index(request) :
    html = ''
    html += '<h1>main page</h1>'
    return HttpResponse(html)

def blog(request) :
    return HttpResponse('Blog')

def html(request) :
    return HttpResponse('HTML Page')

def css(request) :
    return HttpResponse('CSS Page')

def js(request) :
    return HttpResponse('JavaScript Page')


