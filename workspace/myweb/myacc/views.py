from django.shortcuts import render
from myacc.models import AccountBook
from django.shortcuts import HttpResponse

# Create your views here.
def index(request, acc_type=None):
    datas = AccountBook.objects.all()
    if acc_type == 'in':
        datas = datas.filter(inc__gt=0)
    else:
        datas = datas.filter(outc__gt=0)
    context = {
        'datas': datas
    }
    return render(request, 'myacc/index.html', context)
'''
def accTypeSearch(request, acc_type):
    if acc_type == 'in':
        datas = AccountBook.objects.filter(inc__gt=0)
    elif acc_type == 'out':
        datas = AccountBook.objects.filter(outc__gt=0)
    else:
        return HttpResponse('잘못된 요청')
    context = {
        'datas': datas
    }
    return render(request, 'myacc/index.html', context)
'''