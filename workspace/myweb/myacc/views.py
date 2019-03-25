from django.shortcuts import render
from myacc.models import AccountBook
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    datas = AccountBook.objects.all()
    acc_type = request.GET.get('type')
    amount = request.GET.get('amount', 0)

    if acc_type == 'in':
        datas = datas.filter(inc__gte=amount if amount else 0)
    elif acc_type == 'out':
        datas = datas.filter(outc__gte=amount if amount else 0)
    '''if acc_type == 'in':
        if amount:
            datas = datas.filter(inc__gte=amount)
        else:
            datas = datas.filter(inc__gte=0)
    elif acc_type == 'out':
        if amount:
            datas = datas.filter(outc__gte=amount)
        else:
            datas = datas.filter(outc__gte=0)'''
    context = {
        'datas': datas,
        'amount': amount,
        'type': acc_type,
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