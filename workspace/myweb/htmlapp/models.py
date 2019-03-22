from django.db import models

# Create your models here.
class TableName(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    phone = models.CharField(max_length=13, null=False, blank=False)
    home_addr = models.CharField(max_length=50, null=True, blank=True)
    create_date = models.DateField()