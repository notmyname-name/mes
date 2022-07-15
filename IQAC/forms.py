from django import forms
from django.db.models import fields
from django.forms import widgets
from django.http import request
from IQAC.models import *
# IQAC CALENDER OF EVENTS
       
 
class IQAC_COEform(forms.ModelForm):
                                                       
    class Meta:
        model=IQAC_COE_model
        fields='__all__'
       
        


class Aqarform(forms.ModelForm):
                                                       
        class Meta:
            model=Aqar_model
            fields='__all__'
       
           

class MOMform(forms.ModelForm):
                                                       
        class Meta:
            model=MOM_model
            fields='__all__'

#EVENT CONDUCTED ENTRY - IQAC
class iqacEventform(forms.ModelForm):
                                                    
    class Meta:
        model=iqacEvent_model
        fields='__all__'

#IQAC  MEETINGS CONDUCTED ENTRY 
class iqacmeetingform(forms.ModelForm):
                                                    
    class Meta:
        model=iqacmeeting_model
        fields='__all__'


# IQAC MANDATORY DOCUMENTS
       
 
class IQACmandatedocform(forms.ModelForm):
                                                       
    class Meta:
        model=IQACmandatedoc_model
        fields='__all__'
# IQAC Action plan
       
 
class Actioniqacform(forms.ModelForm):
                                                       
    class Meta:
        model=Actioniqac_model
        fields='__all__'

# IQAC MOU
       
 
class Mouiqacform(forms.ModelForm):
                                                       
    class Meta:
        model=Mouiqac_model
        fields='__all__'


# IQAC Infrastructure details
       
 
class Infraiqacform(forms.ModelForm):
                                                       
    class Meta:
        model=Infraiqac_model
        fields='__all__'

# IQAC ADD ON course details
       
 
class addoncourseform(forms.ModelForm):
                                                       
    class Meta:
        model=addoncourse_model
        fields='__all__'

# Audit report details
       
 
class auditRptform(forms.ModelForm):
                                                       
    class Meta:
        model=auditRpt_model
        fields='__all__'

#  Internal Audit report details
       
 
class CollegeauditRptform(forms.ModelForm):
                                                       
    class Meta:
        model=CollegeauditRpt_model
        fields='__all__'

# Student Scholarship
       
 
class scholarshipdetform(forms.ModelForm):
                                                       
    class Meta:
        model=scholarshipdet_model
        fields='__all__'


#Funds recieved from govt/non-govt/management for different purpose



class Financegrantsform(forms.ModelForm):
                                                       
    class Meta:
        model=Financegrants_model
        fields='__all__'
#code of conduct for the stakeholders

class codeconductform(forms.ModelForm):
                                                       
    class Meta:
        model=codeconduct_model
        fields='__all__'
        
#Notifications

class notificationform(forms.ModelForm):
    class Meta:
        model=notification_model
        fields=['message']
    
class LoginPage(forms.Form): 
    
    Username = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={"class": "form-control"})) 
    
    Password = forms.CharField(widget = forms.PasswordInput(attrs={"class": "form-control"})) 
    
   
class memberform(forms.ModelForm):
                                                       
    class Meta:
        model=member_model
        fields='__all__' 