from django.db import models

# Create your models here.
# 테이블 이름 : AccountBook(가계부)
# 컬럼 정보
#     항목      : 문자열(100), 빈 문자열(blank) 허용
#     수입 금액 : 정수, 기본 값 0
#     지출 금액 : 정수, 기본 값 0
#     수량      : 정수, 기본 값 0
#     날짜      : 날짜

'''테이블명.objects.values : 사전
테이블명.objects.values_list : 튜플
테이블명.objects.order_by : 정렬 ('-inc', 'outc' ) 역순'''

class AccountBook(models.Model):
    item = models.CharField(max_length=100, blank=True)
    inc = models.IntegerField(default=0)
    outc = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    date = models.DateField()