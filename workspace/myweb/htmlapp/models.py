from django.db import models

# Create your models here.
class TableName(models.Model):
    id = models.AutoField() # 데이터 자동 증가
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    phone = models.CharField(null=False, blank=False)
    home_addr = models.CharField(null=True, blank=True)
    create_date = models.DateField()