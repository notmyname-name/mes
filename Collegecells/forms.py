from django import forms
from django.forms import widgets
from django.http import request
from Collegecells.models import *

# Cell EVENTS planning
       
 
class cellEventplanform(forms.ModelForm):
         
    def __init__(self,org, *args, **kwargs):
        super(cellEventplanform,self).__init__(*args, **kwargs)
        self.fields['org'].initial = org                                              
    class Meta:
        model=cellEventplan_model
        fields='__all__'
       
        widgets = {
            
            "Year":forms.Select(attrs={"class": "form-control"}),
            "Date":forms.DateInput(attrs={"class": "form-control"}),
            "Name_ev":forms.TextInput(attrs={"class":"form-control"}),
            "Tent_date":forms.TextInput(attrs={"class":"form-control"}),
            "Remarks":forms.TextInput(attrs={"class": "form-control"}),
            "Noofstd":forms.TextInput(attrs={"class": "form-control"}),
            "org" : forms.TextInput(attrs={"class": "form-control"}),
            
            
            
        }



class MOMform(forms.ModelForm):
    def __init__(self,org, *args, **kwargs):
        super(MOMform,self).__init__(*args, **kwargs)
        self.fields['org'].initial = org                                       
    class Meta:
        model=MOM_model
        fields='__all__'
    
        widgets = {
        
        "date":forms.DateInput(attrs={"class": "form-control"}),
        
        "mom":forms.FileInput(attrs={"class": "form-control"}),
        
        "ATR":forms.FileInput(attrs={"class": "form-control"}),
        "org" : forms.TextInput(attrs={"class": "form-control"}),

        
    }
#EVENT CONDUCTED ENTRY - cell/club
class ClubEventform(forms.ModelForm):
    def __init__(self,org, *args, **kwargs):
        super(ClubEventform,self).__init__(*args, **kwargs)
        self.fields['org'].initial = org                                                  
    class Meta:
        model=ClubEvent_model
        fields='__all__'
       
        widgets = {
            "Conduct_for" : forms.Select(attrs={"class": "form-control"}),
            "scope" : forms.Select(attrs={"class": "form-control"}),
            "category" : forms.Select(attrs={"class": "form-control"}),
            "mode":forms.Select(attrs={"class": "form-control"}),
            "year": forms.DateInput(attrs={"class": "form-control"}),
            "Event_Title": forms.TextInput(attrs={"class": "form-control"}),
            "Event_bro": forms.FileInput(attrs={"class": "form-control"}),
            "Event_sche": forms.FileInput(attrs={"class": "form-control"}),
            "Event_Rpt": forms.FileInput(attrs={"class": "form-control"}),
            "Event_photo": forms.FileInput(attrs={"class": "form-control"}),
            "Event_cert": forms.FileInput(attrs={"class": "form-control"}),
            "Event_approval": forms.FileInput(attrs={"class": "form-control"}),
            "Event_misc": forms.FileInput(attrs={"class": "form-control"}),
            "Guest": forms.TextInput(attrs={"class": "form-control"}),
            "Guest_det":forms.FileInput(attrs={"class": "form-control"}),
            "noofstd":forms.TextInput(attrs={"class": "form-control"}),
            "atdlist":forms.FileInput(attrs={"class": "form-control"}),
            "org" : forms.TextInput(attrs={"class": "form-control"}),
        }

class LoginPage(forms.Form): 
    
    Username = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={"class": "form-control"})) 
    
    Password = forms.CharField(widget = forms.PasswordInput(attrs={"class": "form-control"})) 
    
class memberform(forms.ModelForm):
                                                       
    class Meta:
        model=member_model
        fields='__all__' 