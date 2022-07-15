import django_filters
from django_filters import DateFilter

from Collegecells.models import *

class cellEventplan_Filter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "Date", lookup_expr="gte")
    end_date = DateFilter(field_name = "Date", lookup_expr="lte")
    class Meta:
        model = cellEventplan_model
        fields = ["Year"]



class MOM_Filter(django_filters.FilterSet):
    
    class Meta:
        model = MOM_model
        fields = ["date"]


class ClubEvent_Filter(django_filters.FilterSet):
    
    class Meta:
        model = ClubEvent_model
        fields = ["Conduct_for","scope","category","mode"]

