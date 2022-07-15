from django import forms
from django.forms import widgets
from django.http import request
from dept.models import *
#from django.forms import ModelForm



# Subjects of the Department
       
 
class subjectform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(subjectform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                  
    class Meta:
        model=subject_model
        fields='__all__'
       
        widgets = {
            
            "year" : forms.Select(attrs={"class": "form-control"}),
            "clas":forms.Select(attrs={"class": "form-control"}),
            "titlesubject":forms.TextInput(attrs={"class": "form-control"}),
            "tot_no_hrs" : forms.TextInput(attrs={"class":"form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
         }



# Workload  of the Department
       
 
class workldform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(workldform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                    
    class Meta:
        model=workld_model
        fields='__all__'
       
        widgets = {
            
            "year" : forms.Select(attrs={"class": "form-control"}),
            "clas":forms.Select(attrs={"class": "form-control"}),
            "theory_workld":forms.NumberInput(attrs={"class": "form-control"}),
            "pract_workld" :forms.NumberInput(attrs={"class":"form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
         }


# Student Strength  of the Department
       
 
class stdstrengthform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(stdstrengthform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                    
    class Meta:
        model=stdstrength_model
        fields='__all__'
       
        widgets = {
            
            "year" : forms.Select(attrs={"class": "form-control"}),
            "clas":forms.Select(attrs={"class": "form-control"}),
            "no_of_stud":forms.NumberInput(attrs={"class": "form-control"}),
            "combination":forms.TextInput(attrs={"class": "form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
            
         }





# Student Performance -  Departmentwise
       
 
class stdperformform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(stdperformform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                 
    class Meta:
        model=stdperform_model
        fields='__all__'
       
        widgets = {
            "category":forms.Select(attrs={"class":"form-control"}),
            "year" : forms.Select(attrs={"class": "form-control"}),
            "clas":forms.Select(attrs={"class": "form-control"}),
            "combination":forms.TextInput(attrs={"class": "form-control"}),
            "name" : forms.TextInput(attrs={"class": "form-control"}),
            "phnum" : forms.TextInput(attrs={"class": "form-control"}),
            "email" : forms.EmailInput(attrs={"class": "form-control"}),
            "event_title" : forms.TextInput(attrs={"class": "form-control"}),
            "event_details" : forms.TextInput(attrs={"class": "form-control"}),
            "certif": forms.FileInput(attrs={"class": "form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
            
         }


#Student Progression to higher studies - Departmentwise
class stdprogressform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(stdprogressform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                 
    class Meta:
        model=stdprogress_model
        fields='__all__'
       
        widgets = {
            "year":forms.TextInput(attrs={"class": "form-control"}),
            "name":forms.TextInput(attrs={"class": "form-control"}),
            "email":forms.EmailInput(attrs={"class": "form-control"}),
            "phnum":forms.TextInput(attrs={"class": "form-control"}),
            "joinedto":forms.TextInput(attrs={"class": "form-control"}),
            "coursename":forms.TextInput(attrs={"class": "form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
        }





#STUDENT PLACEMENT ENTRY - DEPARTMENTWISE
class stdplacementform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(stdplacementform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                 
    class Meta:
        model=stdplacement_model
        fields='__all__'
       
        widgets = {
            "year":forms.TextInput(attrs={"class": "form-control"}),
            "name":forms.TextInput(attrs={"class": "form-control"}),
            "email":forms.EmailInput(attrs={"class": "form-control"}),
            "phnum":forms.TextInput(attrs={"class": "form-control"}),
            "joinedto":forms.TextInput(attrs={"class": "form-control"}),
            "paypack":forms.TextInput(attrs={"class": "form-control"}),
            "offer_lette": forms.FileInput(attrs={"class": "form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
        }


#EVENT CONDUCTED ENTRY - DEPARTMENTWISE
class deptEventform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(deptEventform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                 
    class Meta:
        model=deptEvent_model
        fields='__all__'
       
        widgets = {
            "Conduct_for" : forms.Select(attrs={"class": "form-control"}),
            "scope" : forms.Select(attrs={"class": "form-control"}),
            "category" : forms.Select(attrs={"class": "form-control"}),
            "mode":forms.Select(attrs={"class": "form-control"}),
            "year": forms.DateInput(attrs={"class": "form-control"}),
            "event_Title": forms.TextInput(attrs={"class": "form-control"}),
            "event_Bro": forms.FileInput(attrs={"class": "form-control"}),
            "event_Sche": forms.FileInput(attrs={"class": "form-control"}),
            "event_Rpt": forms.FileInput(attrs={"class": "form-control"}),
            "event_photo": forms.FileInput(attrs={"class": "form-control"}),
            "event_cert": forms.FileInput(attrs={"class": "form-control"}),
            "event_approval": forms.FileInput(attrs={"class": "form-control"}),
            "event_misc": forms.FileInput(attrs={"class": "form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
        }





#DEPARTMENT MEETINGS CONDUCTED ENTRY - DEPARTMENTWISE
class deptmeetingform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(deptmeetingform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                 
    class Meta:
        model=deptmeeting_model
        fields='__all__'
       
        widgets = {

            "category" : forms.Select(attrs={"class": "form-control"}),
            "year": forms.DateInput(attrs={"class": "form-control"}),
            "agenda": forms.TextInput(attrs={"class": "form-control"}),
            "mom": forms.FileInput(attrs={"class": "form-control"}),
            "atr": forms.FileInput(attrs={"class": "form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
        }


# DEPARTMENT PROJECT PROPOSAL ENTRY 
class deptproposalform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(deptproposalform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                 
    class Meta:
        model=deptproposal_model
        fields='__all__'
       
        widgets = {

            "category" : forms.Select(attrs={"class": "form-control"}),
            "year": forms.DateInput(attrs={"class": "form-control"}),
            "project_title": forms.TextInput(attrs={"class": "form-control"}),
            "agency_name": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.TextInput(attrs={"class": "form-control"}),
            "circular": forms.FileInput(attrs={"class": "form-control"}),
            "proposal": forms.FileInput(attrs={"class": "form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
        }



# 10 STUDENT PROJECT  ENTRY(CURRIULUM MANDATED) - DEPARTMENTWISE 
class studprjform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(studprjform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                 
    class Meta:
        model=studprj_model
        fields='__all__'
       
        widgets = {

            
            "year": forms.DateInput(attrs={"class": "form-control"}),
            "project_title": forms.TextInput(attrs={"class": "form-control"}),
            "no_of_std":forms.TextInput(attrs={"class": "form-control"}),
            "name_of_std": forms.TextInput(attrs={"class": "form-control"}),
            "remarks": forms.TextInput(attrs={"class": "form-control"}),
            "synopsis":forms.FileInput(attrs={"class": "form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
            
            

        }


# 10 DEPARTMENT COMMUNICATION FOR INTERNAL/EXTERNAL GROUP ENTRY
class deptcommform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(deptcommform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                 
    class Meta:
        model=deptcomm_model
        fields='__all__'
       
        widgets = {

            
            "year": forms.DateInput(attrs={"class": "form-control"}),
            "project_title": forms.TextInput(attrs={"class": "form-control"}),
            "no_of_std":forms.TextInput(attrs={"class": "form-control"}),
            "name_of_std": forms.TextInput(attrs={"class": "form-control"}),
            "remarks": forms.TextInput(attrs={"class": "form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),        
            
        }

# Images of the Department
class deptimgesform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(deptimgesform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                 
    class Meta:
        model=deptimges_model
        fields='__all__'
       
        widgets = {

            
            "date": forms.DateInput(attrs={"class": "form-control"}),
            "event_det": forms.TextInput(attrs={"class": "form-control"}),
            "img":forms.FileInput(attrs={"class": "form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
        }




#E-RESOURCES OF DEPARTMENT
       
 
class depteresourceform(forms.ModelForm):
    def __init__(self,dept, *args, **kwargs):
        super(depteresourceform,self).__init__(*args, **kwargs)
        self.fields['dept'].initial = dept                                                    
    class Meta:
        model=depteresource_model
        fields='__all__'
       
        widgets = {
            
            "year" : forms.Select(attrs={"class": "form-control"}),
            "clas":forms.Select(attrs={"class": "form-control"}),
            #"Titlesubject":forms.TextInput(attrs={"class": "form-control"}),


            "pract_manual":forms.FileInput(attrs={"class": "form-control"}),
            "e_book":forms.FileInput(attrs={"class": "form-control"}),
            "video":forms.FileInput(attrs={"class": "form-control"}),
            "qp":forms.FileInput(attrs={"class": "form-control"}),
            "solvedQP":forms.FileInput(attrs={"class": "form-control"}),
            "study_mat":forms.FileInput(attrs={"class": "form-control"}),
            "others":forms.FileInput(attrs={"class": "form-control"}),
            "dept" : forms.TextInput(attrs={"class": "form-control"}),
        }
        
        

class LoginPage(forms.Form): 
    
    Department = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={"class": "form-control"})) 
    
    password = forms.CharField(widget = forms.PasswordInput(attrs={"class": "form-control"})) 

class memberform(forms.ModelForm):
                                                       
    class Meta:
        model=dept
        fields='__all__' 