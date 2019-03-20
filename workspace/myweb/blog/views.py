from django.shortcuts import render

# Create your views here.
def blog(request) :
    return render(request, 'blog/index.html')

def write(request) :
    return render(request, 'html/write.html')