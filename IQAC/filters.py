import django_filters
from django_filters import DateFilter

from IQAC.models import *

class IQAC_COE_Filter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "Date", lookup_expr="gte")
    end_date = DateFilter(field_name = "Date", lookup_expr="lte")
    class Meta:
        model = IQAC_COE_model
        fields = ["Year"]

class Aqar_Filter(django_filters.FilterSet):
    
    class Meta:
        model = Aqar_model
        fields = ["Year"]

class MOM_Filter(django_filters.FilterSet):
    
    class Meta:
        model = MOM_model
        fields = ["date"]


class iqacmeeting_Filter(django_filters.FilterSet):
    
    class Meta:
        model = iqacmeeting_model
        fields = ["category"]

class iqacEvent_Filter(django_filters.FilterSet):
    
    class Meta:
        model = iqacEvent_model
        fields = ["Conduct_for","scope","category","mode"]
        
class IQACmandatedoc_Filter(django_filters.FilterSet):
    
    class Meta:
        model = IQACmandatedoc_model
        fields = ["year"]

class Actioniqac_Filter(django_filters.FilterSet):
    
    class Meta:
        model = Actioniqac_model
        fields = ["year"]

class Mouiqac_Filter(django_filters.FilterSet):
    
    class Meta:
        model = Mouiqac_model
        fields = ["year"]
        
class Infraiqac_Filter(django_filters.FilterSet):
    
    class Meta:
        model = Infraiqac_model
        fields = ["year"]

class addoncourse_Filter(django_filters.FilterSet):
    
    class Meta:
        model = addoncourse_model
        fields = ["Type","year"]

class auditRpt_Filter(django_filters.FilterSet):
    
    class Meta:
        model = auditRpt_model
        fields = ["year"]

class CollegeauditRpt_Filter(django_filters.FilterSet):
    class Meta:
        model = CollegeauditRpt_model
        fields=["year"]
        
class scholarshipdet_Filter(django_filters.FilterSet):
    class Meta:
        model = scholarshipdet_model
        fields = ["year","typ"]
        
class Financegrants_Filter(django_filters.FilterSet):
    class Meta:
        model = Financegrants_model
        fields = ["year","typ"]
        
class codeconduct_Filter(django_filters.FilterSet):
    class Meta:
        model = codeconduct_model
        fields = ["year","codefor"]
        
class notification_Filter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "date", lookup_expr="gte")
    end_date = DateFilter(field_name = "date", lookup_expr="lte")
    class Meta:
        model = notification_model
        fields = []