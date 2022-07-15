from django import forms
from django.forms import widgets
from .models import *
# from .models import STUDENT_DB

class user_FORM(forms.ModelForm):
    class Meta:
        model = user_model
        fields = '__all__'
        widgets = { 
            "verified":forms.HiddenInput(),
            "is_conviner":forms.HiddenInput(),
            
        }
class MagazineForm(forms.ModelForm):
    
        
    class Meta:
        model = ABC
        fields = '__all__'
        widgets = { 
            "name":forms.HiddenInput(),
            "remarks":forms.HiddenInput(),
            "is_approved":forms.HiddenInput(),
            "doc":forms.FileInput(attrs={'accept':'application/pdf'}),
            
        }
class ConvinerMagazineForm(forms.ModelForm):
    
    
    class Meta:
        model = ABC
        fields = '__all__'
        widgets = { 
            "doc":forms.FileInput(attrs={'accept':'application/pdf'}),
        }
        
class LoginPage(forms.Form): 
    
    Username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"})) 
    
    password = forms.CharField(widget = forms.PasswordInput(attrs={"class": "form-control"})) 
    
class verify_FORM(forms.ModelForm):
    class Meta:
        model = user_model
        fields = '__all__'
        widgets = { 
            "name":forms.TextInput(attrs={'readonly': 'readonly'}),
            "email":forms.TextInput(attrs={'readonly': 'readonly'}),
            "phone_no":forms.TextInput(attrs={'readonly': 'readonly'}),
            "year":forms.TextInput(attrs={'readonly': 'readonly'}),
            "sem":forms.TextInput(attrs={'readonly': 'readonly'}),
            "stream":forms.TextInput(attrs={'readonly': 'readonly'}),
            "comb":forms.TextInput(attrs={'readonly': 'readonly'}),
            "sec":forms.TextInput(attrs={'readonly': 'readonly'}),
            "username":forms.TextInput(attrs={'readonly': 'readonly'}),
            "password":forms.TextInput(attrs={'readonly': 'readonly'}),
            "verified":forms.CheckboxInput(),
            "is_conviner":forms.CheckboxInput(),
            
        }