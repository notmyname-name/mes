from django.db import models
from django.db.models.enums import Choices
import dept.models as md 
# Create your models here.
class login_model(models.Model):
    name=models.CharField(max_length=100,verbose_name='Name')
    staff=models.CharField(max_length=100,verbose_name='Phone Number',primary_key=True)
    faculty=models.CharField(max_length=100,verbose_name="Faculty", null=True)
    dept=models.CharField(max_length=100,verbose_name="Department", null=True)
    password=models.CharField(max_length=100,verbose_name='Password')
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class profile_model(models.Model):
    deptList=md.dept.objects.values_list('dept',flat=True)
    
    choice=tuple([tuple([str(i),str(i)]) for i in deptList])
    print(choice)
    # choice=(("1","1"),("2","2"))
    dept=models.CharField(max_length=10,verbose_name='Department',choices=choice)
    name=models.CharField(max_length=100,verbose_name='Name of the Staff')
    
    qualification=models.CharField(max_length=100,verbose_name='Qualification of the Staff ')
    designation=models.CharField(max_length=100,verbose_name='Designation',choices=(("HOD","HOD"),("Lecturer","Lecturer")))
    num=models.CharField(max_length=100,verbose_name='Phone Number')
    dob=models.DateField(verbose_name='Date of Birth')
    doj=models.DateField(verbose_name='Date of joining MESACS')
    pan=models.CharField(max_length=100,verbose_name='PAN number')
    aadhar=models.CharField(max_length=100,verbose_name='AAdhar Number')
    email=models.EmailField(verbose_name='Email ID')
    address=models.TextField(verbose_name='Address')
    photo=models.ImageField(upload_to='images',verbose_name='Photos')
    tenth_markscard=models.FileField(upload_to="files", verbose_name="Tenth Marks Card", null="True",blank="True",)
    pu_markscard=models.FileField(upload_to="files", verbose_name="PU Marks Card", null="True",blank="True")
    degree_markscard=models.FileField(upload_to="files", verbose_name="Degree Marks Card", null="True",blank="True")
    master_markscard=models.FileField(upload_to="files", verbose_name="Master's Marks Card", null="True",blank="True")
    mphill_markscard=models.FileField(upload_to="files", verbose_name="MPhill's Marks Card", null="True",blank="True")
    phd_markscard=models.FileField(upload_to="files", verbose_name="Phd Marks Card", null="True",blank="True")
    apppointment_letter=models.FileField(upload_to="files", verbose_name="Appointment Letter", null="True",blank="True")
    resume=models.FileField(upload_to="files", verbose_name="Resume", null="True")
    username=models.CharField(max_length=100,verbose_name='Username',primary_key=True)
    password=models.CharField(max_length=100,verbose_name='Password')
    def __str__(self):
        return self.username
    



    
class aad_model(models.Model):
    choice=(
    ("Seminar", "Seminar"),
    ("Workshop", "Workshop"),
    ("Conference attendance", "Conference attendance"),
    ("Paper Presentation attendance", "Paper Presentation attendance"),
    ("Faculty Development Program", "Faculty Development Program"),
    ("Referesher","Referesher"),
    ("Orientation Prg Attended","Orientation Prg Attended"),
    ("Others if any","Others if any"),)
    option=models.CharField(max_length=100,choices = choice,verbose_name="Event")
    date=models.DateField(verbose_name='Date')
    document=models.FileField(upload_to="files", verbose_name="Document", null="True")
    staff=models.ForeignKey(profile_model,on_delete=models.CASCADE, null="True",blank="True")
    
    def __str__(self):
        return self.option
    
class misc_model(models.Model):
    choice=(
    ("Guest of Honours", "Guest of Honours"),
    ("Awards", "Awards"),
    ("Apreciation", "Appreciation"),
    ("Lectures Given", "Lectures Given"),
    ("Faculty Development conducted", "Faculty Development conducted"),
    ("Any Other Relevant","Any Other Relevant"),)
    option=models.CharField(max_length=100,choices = choice,verbose_name="Achievement")
    date=models.DateField(verbose_name='Date')
    document=models.FileField(upload_to="files", verbose_name="Document", null="True")
    staff=models.ForeignKey(profile_model,on_delete=models.CASCADE, null="True",blank="True")
    def __str__(self):
        return self.option

class univ_model(models.Model):
    choice=(
    ("BOS", "BOS"),
    ("BOE", "BOE"),
    ("Valuation", "Valuation"),
    ("Others if any","Others if any"),)
    option=models.CharField(max_length=100,choices = choice,verbose_name="Activities")
    date=models.DateField(verbose_name='Date')
    document=models.FileField(upload_to="files", verbose_name="Document", null="True")
    staff=models.ForeignKey(profile_model,on_delete=models.CASCADE, null="True",blank="True")
    def __str__(self):
        return self.option

class pub_model(models.Model):
    choice=(
    ("Publication of staff in the Journals notified on UGC Website", "Publication of staff in the Journals notified on UGC Website"),
    ("Publication of staff in National/International Conference Prooceedings", "Publication of staff in National/International Conference Prooceedings"),
    ("Publication of staff in the Books and Book Chapters in Edited Volume", "Publication of staff in the Books and Book Chapters in Edited Volume"),
    ("Others if any","Others if any"),)
    option=models.CharField(max_length=100,verbose_name="Publication in",choices=choice)
    dept=models.CharField(max_length=10,verbose_name='Department')
    title=models.CharField(max_length=100,verbose_name='Title')
    name=models.CharField(max_length=100,verbose_name='Name of the author/s')
    num=models.CharField(max_length=100,verbose_name='Number of the Journal/Chapter')
    year=models.CharField(max_length=100,verbose_name='Year of publication')
    issn=models.CharField(max_length=100,verbose_name='ISSN/ISBN Number')
    pubname=models.CharField(max_length=100,verbose_name='Name of the Publisher',blank=True)
    document=models.FileField(upload_to="files",verbose_name='Upload UGC enlistment of the Journal')
    staff=models.ForeignKey(profile_model,on_delete=models.CASCADE, null="True",blank="True")
    def __str__(self):
        return self.title
    
class port_model(models.Model):
    name=models.CharField(max_length=100,verbose_name='Portfolio Name')
    year=models.CharField(max_length=10,verbose_name='Year')
    
    
    desc=models.TextField(verbose_name='Descprition in 500 words')
    staff=models.ForeignKey(profile_model,on_delete=models.CASCADE, null="True",blank="True")
    def __str__(self):
        return self.name
