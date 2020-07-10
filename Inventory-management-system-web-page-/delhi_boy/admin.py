from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import goods


class QuestionAdmin(admin.ModelAdmin):
    fields = ['serial_no','equipment_name','information','software_ver','begin_date','expiry_date','is_obj_under_amc','quantity']

admin.site.register(goods, QuestionAdmin)
