import django_tables2 as tables
from .models import goods

class SimpleTable(tables.Table):
    class Meta:
        model = goods