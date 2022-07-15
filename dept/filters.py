import django_filters
from django_filters import DateFilter

from dept.models import *

class subject_Filter(django_filters.FilterSet):
    
    class Meta:
        model = subject_model
        fields = ["year","clas"]

class workld_Filter(django_filters.FilterSet):
    
    class Meta:
        model = workld_model
        fields = ["year","clas"]

class stdstrength_Filter(django_filters.FilterSet):
    
    class Meta:
        model = stdstrength_model
        fields = ["year","clas"]


class stdperform_Filter(django_filters.FilterSet):
    
    class Meta:
        model = stdperform_model
        fields = ["category","year","clas"]

class stdprogress_Filter(django_filters.FilterSet):
    
    class Meta:
        model = stdprogress_model
        fields = ["year"]
        
class stdplacement_Filter(django_filters.FilterSet):
    
    class Meta:
        model = stdplacement_model
        fields = ["year"]

class deptEvent_Filter(django_filters.FilterSet):
    
    class Meta:
        model = deptEvent_model
        fields = ["conduct_for","scope","category","mode"]

class deptmeeting_Filter(django_filters.FilterSet):
    
    class Meta:
        model = deptmeeting_model
        fields = ["category"]
        
class deptproposal_Filter(django_filters.FilterSet):
    
    class Meta:
        model = deptproposal_model
        fields = ["category"]

class studprj_Filter(django_filters.FilterSet):
    
    class Meta:
        model = studprj_model
        fields = ["year"]

class deptcomm_Filter(django_filters.FilterSet):
    
    class Meta:
        model = deptcomm_model
        fields = ["comm_to"]

class deptimges_Filter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "date", lookup_expr="gte")
    end_date = DateFilter(field_name = "date", lookup_expr="lte")
    class Meta:
        model = deptimges_model
        fields=[]
class depteresource_Filter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "date", lookup_expr="gte")
    end_date = DateFilter(field_name = "date", lookup_expr="lte")
    class Meta:
        model = depteresource_model
        fields = ["year","clas"]