
from django import forms
import dept.models as md 
# from django.db.models.enums import Choices
# from django.forms import fields, widgets
# from django.http import request


from staff.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class profileForm(forms.ModelForm):
    
        

                                         
    class Meta:
        model=profile_model
        fields='__all__'
        # widgets={
        #     "name":forms.TextInput(attrs={"value":request.POST['Name']}),
        #     "num":forms.TextInput(attrs={"value":request.POST['Number']})
        # }
        widgets = {
            
            "dept" : forms.Select(attrs={"class": "form-control"}),
            "name" : forms.TextInput(attrs={"class": "form-control"}),
            "qualification" : forms.TextInput(attrs={"class": "form-control"}),
            "designation" : forms.Select(attrs={"class": "form-control"}),
            "num" : forms.TextInput(attrs={"class": "form-control"}),
            "dob" : DateInput(attrs={"class": "form-control"}),
            "doj" : DateInput(attrs={"class": "form-control"}),
            "pan" : forms.TextInput(attrs={"class": "form-control"}),
            "aadhar" : forms.TextInput(attrs={"class": "form-control"}),
            "email" : forms.EmailInput(attrs={"class": "form-control"}),
            "address" : forms.TextInput(attrs={"class": "form-control"}),
            "photo" : forms.FileInput(attrs={"class": "form-control"}),
            "tenth_markscard": forms.FileInput(attrs={"class": "form-control"}),
            "pu_markscard": forms.FileInput(attrs={"class": "form-control"}),
            "degree_markscard": forms.FileInput(attrs={"class": "form-control"}),
            "master_markscard": forms.FileInput(attrs={"class": "form-control"}),
            "mphill_markscard": forms.FileInput(attrs={"class": "form-control"}),
            "phd_markscard": forms.FileInput(attrs={"class": "form-control"}),
            "apppointment_letter": forms.FileInput(attrs={"class": "form-control"}),
            "resume": forms.FileInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.TextInput(attrs={"class": "form-control"}),
        }
        

class LoginPage(forms.Form): 
    deptList=md.dept.objects.values_list('dept',flat=True)
    
    choice=tuple([tuple([str(i),str(i)]) for i in deptList])
    print(choice)
    # choice=(("1","1"),("2","2"))
    Username = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={"class": "form-control"})) 
    Department = forms.CharField(max_length = 200, widget=forms.Select(attrs={"class": "form-control"},choices=choice)) 
    password = forms.CharField(widget = forms.PasswordInput(attrs={"class": "form-control"})) 
    
class aadForm(forms.ModelForm):
    def __init__(self,staff, *args, **kwargs):
        super(aadForm,self).__init__(*args, **kwargs)
        self.fields['staff'].initial = staff  
    class Meta:
        model=aad_model
        fields='__all__'
        widgets = {
            "option" : forms.Select(attrs={"class": "form-control"}),
            "date":DateInput(attrs={"class": "form-control"}),
            "staff" : forms.TextInput(attrs={"class": "form-control"}),
            
            "document" : forms.FileInput(attrs={"class": "form-control"}),
        }
        
        
class miscForm(forms.ModelForm):
    def __init__(self,staff, *args, **kwargs):
        super(miscForm,self).__init__(*args, **kwargs)
        self.fields['staff'].initial = staff  
    class Meta:
        model=misc_model
        fields='__all__'
        widgets = {
            "option" : forms.Select(attrs={"class": "form-control"}),
            "date":forms.DateInput(attrs={"class": "form-control"}),
            "staff" : forms.TextInput(attrs={"class": "form-control"}),
            "document" : forms.FileInput(attrs={"class": "form-control"}),
        }
         
         
class univForm(forms.ModelForm):
    def __init__(self,staff, *args, **kwargs):
        super(univForm,self).__init__(*args, **kwargs)
        self.fields['staff'].initial = staff  
    class Meta:
        model=univ_model
        fields='__all__'
        widgets = {
            "option" : forms.Select(attrs={"class": "form-control"}),
            "date":forms.DateInput(attrs={"class": "form-control"}),
            "staff" : forms.TextInput(attrs={"class": "form-control"}),
            "document" : forms.FileInput(attrs={"class": "form-control"}),
        }
        
class pubForm(forms.ModelForm):
    def __init__(self,staff, *args, **kwargs):
        super(pubForm,self).__init__(*args, **kwargs)
        self.fields['staff'].initial = staff  
    class Meta:
        model=pub_model
        fields='__all__'
        widgets={
            "option":forms.Select(attrs={"class": "form-control"}),
            "dept":forms.TextInput(attrs={"class": "form-control"}),
            "title":forms.TextInput(attrs={"class": "form-control"}),
            "name":forms.TextInput(attrs={"class": "form-control"}),
            "num":forms.TextInput(attrs={"class": "form-control"}),
            "year":forms.TextInput(attrs={"class": "form-control"}),
            "issn":forms.TextInput(attrs={"class": "form-control"}),
            "pubname":forms.TextInput(attrs={"class": "form-control","placeholder":"Optional"}),
            "document":forms.FileInput(attrs={"class": "form-control"}),
            "staff" : forms.TextInput(attrs={"class": "form-control"}),
        }
class portForm(forms.ModelForm):
    def __init__(self,staff, *args, **kwargs):
        super(portForm,self).__init__(*args, **kwargs)
        self.fields['staff'].initial = staff  
    class Meta:
        model=port_model
        fields='__all__'
        widgets = {
            "name" : forms.TextInput(attrs={"class": "form-control"}),
            "year":forms.TextInput(attrs={"class": "form-control"}),
            "staff" : forms.TextInput(attrs={"class": "form-control"}),
            "desc" : forms.TextInput(attrs={"class": "form-control"}),
        }
         