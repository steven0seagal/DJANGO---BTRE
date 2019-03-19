import django_tables2 as tables
from .models import Listing

class PersonTable(tables.Table):
    class Meta:
        model = Listing
        template_name = 'django_tables2/bootstrap.html'