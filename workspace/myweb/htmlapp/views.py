from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def html(request) :
    return render(request, 'htmlapp/index.html')

def html2(request) :
    return render(request, 'html/html2.html')

def tagExample(request, tag_num) :
    data = {
        1: {'tag': 'a', 'example': '<a href="www.xxx.com">사이트</a>'},
        2: {'tag': 'b', 'example': '<b>볼드</b>'},
        3: {'tag': 'li', 'example': '<li>목록</li>'},
    }

    context = {
        'tags': '1', 'content': '2', 'data_list': [1,2,3]
    }

    return render(request, 'htmlapp/view.html', context) #사전에서 get함수의 인자로 key를 넘겨주면 value 값을 추출할 수 있음