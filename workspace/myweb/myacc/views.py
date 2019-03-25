from django.shortcuts import render
from myacc.models import AccountBook

# Create your views here.
def index(request):
    datas = AccountBook.objects.all()
    context = {
        'datas': datas
    }
    return render(request, 'myacc/index.html', context)