from django.shortcuts import render

# Create your views here.
def blog(request) :
    return render(request, 'blog/index.html')

def write(request) :
    return render(request, 'html/write.html')

'''def intro(request):
    return render(request, 'blog/intro.html')

def syntax(request):
    return render (request, 'blog/syntax.html')'''

def title(request): #하나의 함수에서 GET, POST 요청 분기
    if request.method == 'GET':
        data = request.GET.get('name') #GET 방식으로 요청 받은 URL. 여러 파라미터 중 어떤 걸 가져올지 파라미터 명시.
        ver = request.GET.get('ver')
    elif request.method == 'POST':
        data = request.POST.get('name')
        ver = request.POST.get('ver')
    context = {
        'data': data,
        'version' : ver
    }
    return render(request, 'blog/title.html', context)

def inputForm(request):
    if request.method == 'GET':
        return render(request, 'blog/form.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        _type = request.POST.get('type')
        note = request.POST.get('note')
        gender = request.POST.get('gender')
        #purpose = request.POST.get('purpose')
        purpose = request.POST.getlist('purpose')
        
        from django.shortcuts import HttpResponse
        return HttpResponse(f'{title} / {_type} / {note} / {gender} / {purpose}')
    '''context = {
        'title' : title,
        '_type' : _type,
        'note' : note,
        'gender' : gender,
        'purpose' : purpose,
    }
    return render(request, 'blog/form.html', context)'''