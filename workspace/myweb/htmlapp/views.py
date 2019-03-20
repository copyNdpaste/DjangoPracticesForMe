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
        'tags': '1', 'content': '2', 'data_list': [1,2,3],
        'data_dict': {'name': '홍길동', 'age': 99, 'blood': 'B'},
    }

    return render(request, 'htmlapp/view.html', context) #사전에서 get함수의 인자로 key를 넘겨주면 value 값을 추출할 수 있음

def tagTitle(request, title=None) :
    from django.core.files.storage import FileSystemStorage

    fs = FileSystemStorage()
    fs.location = 'C:\\Django_Practice_For_MH\\workspace\\myweb\\htmlapp\\templates'
    if title == None:
        # 저장되어 있는 파일 목록 출력
        data = fs.listdir('docs')
    else:
        # title에 지정된 파일을 불러옴
        data = fs.open(f'docs\\{title}').read()
        data = str(data, encoding='utf-8')
        return render(request, 'htmlapp/view.html', {'data': data})
    '''fo = open('C:\\Django_Practice_For_MH\\workspace\\myweb\\htmlapp\\templates\\docs\\' + title, 'r', encoding='utf-8')
    context = {
        'data': fo.read()
    }
    fo.close()
    return render(request, 'htmlapp/view.html', context)'''
    
    context = { 
        'data' : data
    }
    return render(request, 'htmlapp/tag_list.html', context)