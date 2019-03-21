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

def title(request):
    data = request.GET.get('name') #GET 방식으로 요청 받은 URL. 여러 파라미터 중 어떤 걸 가져올지 파라미터 명시.
    ver = request.GET.get('ver')
    context = {
        'data': data,
        'version' : ver
    }
    return render(request, 'blog/title.html', context)