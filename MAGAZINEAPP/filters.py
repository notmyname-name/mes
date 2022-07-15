import django_filters
from django_filters import DateFilter

from .models import ABC

class SearchFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "date_and_time", lookup_expr="gte")
    end_date = DateFilter(field_name = "date_and_time", lookup_expr="lte")
    class Meta:
        model = ABC
        fields = ["doc_type","is_approved"]
