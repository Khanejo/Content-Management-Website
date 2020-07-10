from django.db import models
from datetime import date

# Create your models here.

class goods(models.Model):
    serial_no = models.CharField(primary_key=True,max_length=100)
    equipment_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    software_ver=models.CharField(max_length=32,blank=True)
    information = models.CharField(max_length = 200)
    begin_date =models.DateField(null=True,blank=True)
    expiry_date = models.DateField(null=True,blank=True)
    is_obj_under_amc = models.BooleanField(default=True)
    
    class Meta:
        db_table="goods"




