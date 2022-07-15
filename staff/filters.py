import django_filters


from staff.models import *

class aad_Filter(django_filters.FilterSet):
    
    class Meta:
        model = aad_model
        fields = ["option"]

class univ_Filter(django_filters.FilterSet):
    
    class Meta:
        model = univ_model
        fields = ["option"]

class misc_Filter(django_filters.FilterSet):
    
    class Meta:
        model = misc_model
        fields = ["option"]

class pub_Filter(django_filters.FilterSet):
    
    class Meta:
        model = pub_model
        fields = ["option"]
        
class port_Filter(django_filters.FilterSet):
    
    class Meta:
        model = port_model
        fields = ["name"]