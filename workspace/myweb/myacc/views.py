from django.shortcuts import render, HttpResponse, redirect
from myacc.models import AccountBook

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

def insert(request):
    if request.method == 'GET':
        # 양식 페이지 전달
        return render(request, 'myacc/insert.html')
    elif request.method == 'POST':
        # 사용자 입력 정보 DB에 저장
        record = AccountBook()
        record.item = request.POST.get('item')
        record.inc = request.POST.get('inc')
        record.outc = request.POST.get('outc')
        record.count = request.POST.get('count')
        record.date = request.POST.get('date')
        record.save()

        return redirect('/myacc/')

        context = {
            'success': '저장 완료',
        }
    #return render(request, 'myacc/insert.html', context)
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