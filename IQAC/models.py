from django.db import models

# Create your models here.


#1 CALENDER OF EVENTS ENTRY

class IQAC_COE_model(models.Model):
    YR_choice=[
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        
    ]
    
    Year=models.CharField(max_length=15, choices=YR_choice, null=True,verbose_name='Year')
    Date=models.DateField(verbose_name='date of entry')
    Name_ev=models.CharField(max_length=200,  null=True,verbose_name='Name of the Event')
    Tent_date=models.CharField(max_length=200,  null=True,verbose_name='Tentative date of the Event')
   # Faculty=
    # Department= FORIEGN KEY INTRODUTION CAN WE THINK

    Remarks=models.CharField(max_length=200,  null=True,verbose_name='Remarks')
    COE_univ=models.FileField(upload_to="files", verbose_name="Calender of Events - UNIVERSITY")





# 2 Aqar Reports
class Aqar_model(models.Model):
    Year=models.CharField(max_length=15, verbose_name="Year of AQAR")
    Aqarupload=models.FileField(upload_to="files",verbose_name="Upload Your AQAR")
    NAACACK=models.FileField(upload_to="files",verbose_name="Upload your NAAC Acknowledgement")
    
# 3 Minutes of meeting of IQAC
class MOM_model(models.Model):
    date=models.DateField(verbose_name='Date conducted')
    mom=models.FileField(upload_to="files",verbose_name="Minutes of meeting")
    ATR=models.FileField(upload_to="files",verbose_name="Action taken Report")
    

# 4 IQAC MEETINGS ENTRY 
class iqacmeeting_model(models.Model):
     type_choice=[
        
        ('All staff_meet', 'All Staff Meeting'),
        ('IQAC member_meet', 'IQAC Members Meeting'),
        ('Office member_meet', 'Office Staff Meeting'),
        ('std_meet','staff Student Meeting'),
                   
     ]
     category=models.CharField(max_length=30, choices=type_choice, null=True,verbose_name='Meeting category')
     year=models.DateField(verbose_name='Date conducted')
     Agenda=models.CharField(max_length=100,verbose_name='Agenda of the Meeting')
     MOM=models.FileField(upload_to="files", verbose_name='Minutes of Meeting')
     ATR=models.FileField(upload_to="files", verbose_name='Action Taken Report')



#5 EVENTS OF IQAC ENTRY - Quality intiatives by IQAC


class iqacEvent_model(models.Model):
    ty1_choice=[
        
        ('std', ' Students'),
        ('staff', ' Staff'),
            
        
    ]
    type_choice=[
        
        ('FDP', 'Faculty Development Program'),
        ('GL', 'Guest Lecture'),
        ('CONF', 'Conference'),
        ('WORKSP', 'workshop'),
        ('SEMINAR', 'seminar'),
        ('HANDON', 'Hands on'),
        ('WEBINAR', 'webinar'),
        ('other','oth')
               
        ]


    scope_choice=[
        
        ('Int', 'International'),
        ('Nation', 'National'),
        ('State', 'State'),
        ('int_class', 'Inter  Class Event'),
        ('int_faculty', 'Inter faculty Event'),
        ('int_college', 'Intercolligiate'),
                  
        
    ]
    m_choice=[
        
        ('online','Online'),
        ('off','Offline'),
    ]
    Conduct_for=models.CharField(max_length=30, choices=ty1_choice, null=True ,verbose_name='Event Conducted for')
    scope=models.CharField(max_length=30, choices=scope_choice,null=True,verbose_name='Type/Scope of the Event')
    category=models.CharField(max_length=30, choices=type_choice, null=True,verbose_name='Event category')
    mode=models.CharField(max_length=30, choices=m_choice, null=True,verbose_name='Mode of conducting Event')
    year=models.DateField(verbose_name='Date conducted')
    Event_Title=models.CharField(max_length=100,verbose_name='Title of the Event')
    Event_bro=models.FileField(upload_to="files", verbose_name="Brouchure")
    Event_sche=models.FileField(upload_to="files", verbose_name="Event Schedule")
    Event_Rpt=models.FileField(upload_to="files", verbose_name="Event Report")
    Event_photo=models.FileField(upload_to="files", verbose_name="Event Photos")
    Event_cert=models.FileField(upload_to="files", verbose_name="Event Sample Certificate")
    Event_approval=models.FileField(upload_to="files", verbose_name="Event Approval/Statuory letter")
    Event_misc=models.FileField(upload_to="files", verbose_name="Event Miscellaneous")





# 6 IQAC Mandatory/Statuory Document entries

class IQACmandatedoc_model(models.Model):
    year=models.CharField(max_length=30, verbose_name='Year')
    COE_Univ=models.FileField(upload_to="files",verbose_name='Calender of Events - Univeristy')
    COE_IQAC=models.FileField(upload_to="files",verbose_name='Calender of Events -IQAC')
    Cir_Univ=models.FileField(upload_to="files",verbose_name='Circular - Univeristy')
    Cir_UGC=models.FileField(upload_to="files",verbose_name='Circular-UGC')
    ugc=models.FileField(upload_to="files",verbose_name='UGC 2f/12(B) certificate')
    affiliation=models.FileField(upload_to="files",verbose_name='College Affiliation')
    TT_col_test=models.FileField(upload_to="files",verbose_name='Time Table - Internal College Test') 
    TT_College=models.FileField(upload_to="files",verbose_name='Time Table - College')
    Others=models.FileField(upload_to="files", verbose_name="Any other relevant material")
   

# 7 IQAC Action plan 
class Actioniqac_model(models.Model):
    year=models.CharField(max_length=30, verbose_name='Year')
    plan=models.CharField(max_length=250, verbose_name="Plan of Action")



# 8 IQAC MOU's
class Mouiqac_model(models.Model):
    year=models.CharField(max_length=30, verbose_name='Year')
    Purp=models.CharField(max_length=100, verbose_name='Purpose of the MOU')
    Dept=models.CharField(max_length=30, verbose_name='Involved Department/ Cell/ Club')
    Moucpy=models.FileField(upload_to="files", verbose_name="MOU Copy ")

# 9 IQAC Details of Infrastructure Augmentation
class Infraiqac_model(models.Model):
    year=models.CharField(max_length=30, verbose_name='Year')
    Typeinf=models.CharField(max_length=100, verbose_name='Type of Augmented infrastructure')
    Dept=models.CharField(max_length=30, verbose_name='Involved Department/ Cell/ Club')
    Invoicecpy=models.FileField(upload_to="files",verbose_name="Invoice Copy upload")
    remark=models.CharField(max_length=250, verbose_name='Remarks')
    img=models.ImageField(upload_to='images',verbose_name=' Supporting Photos')




# 10 IQAC Details of Add on Courses
class addoncourse_model(models.Model):
    Course_type=[
        
        ('Certificate','Certificate'),
        ('Diploma','Diploma'),
        ('others','others')
    ]
    year=models.CharField(max_length=30, verbose_name='Year')
    Type=models.CharField(max_length=100, choices=Course_type,verbose_name='Type of Course')
    Dept=models.CharField(max_length=30, verbose_name='Involved Department/ Cell/ Club')
    rptcpy=models.FileField(upload_to="files",verbose_name="Copy of the Report from the Department")
    remark=models.CharField(max_length=250, verbose_name='Remarks')
    img=models.ImageField(upload_to='images',verbose_name=' Supporting Photos')



# 11 Financial Audit Report of the college
class auditRpt_model(models.Model):
    
    year=models.CharField(max_length=30, verbose_name='Year')
    
    rptcpy=models.FileField(upload_to="files", verbose_name="Copy of the Report from the Management")
    remark=models.CharField(max_length=250, verbose_name='Remarks')





# 12 Other Audit Report of the college
class CollegeauditRpt_model(models.Model):
    
    year=models.CharField(max_length=30, verbose_name='Year')
    
    frptcpy=models.FileField(upload_to="files", verbose_name="Internal financial Audit Report of the College")
    Grptcpy=models.FileField(upload_to="files", verbose_name="Green Audit Report of the College")
    Erptcpy=models.FileField(upload_to="files", verbose_name="Energy Audit Report of the College")
    Arptcpy=models.FileField(upload_to="files", verbose_name="Academic Audit Report of the College")
    remark=models.CharField(max_length=250, verbose_name='Remarks')
  

# 13 Scholarship details
class scholarshipdet_model(models.Model):
    scholarship_type=[
        
        ('Government','Govt'),
        ('Non-Government','Non-Govt'),
        ('others','others')
    ]
    year=models.CharField(max_length=30, verbose_name='Year')
    typ=models.CharField(max_length=30, choices=scholarship_type,null=True,verbose_name='Type of the Scholarship')
    name=models.CharField(max_length=30, verbose_name='Name of the Scholarship')
    amt=models.CharField(max_length=30, verbose_name='Amount distruted')
    Stdlist=models.FileField(upload_to="files", verbose_name="Names of the Students")
    remark=models.CharField(max_length=250, verbose_name='Remarks')



#14 Funds/grants recieved from govt/non-govt/management for different purpose
class Financegrants_model(models.Model):
    grant_type=[
        
        ('Government','Govt'),
        ('Non-Government','Non-Govt'),
        ('others','others')
    ]
    year=models.CharField(max_length=30, verbose_name='Year')
    typ=models.CharField(max_length=30, choices=grant_type,null=True,verbose_name='Type of the Grant')
    name=models.CharField(max_length=30, verbose_name='Name of the Grant')
    amt=models.CharField(max_length=30, verbose_name='Amount Sanctioned')
    dept=models.CharField(max_length=30, verbose_name='Department Involved')
    Grantdoc=models.FileField(upload_to="files", verbose_name="Document showing the sanction")
    other=models.FileField(upload_to="files", verbose_name="Any other document relevant")
    remark=models.CharField(max_length=250, verbose_name='Remarks')


#15 Code of conduct entry
class codeconduct_model(models.Model):
    code_type=[
        
        ('Teacher','Teacher'),
        ('Student','Student'),
        ('others','others')
    ]
    year=models.CharField(max_length=30, verbose_name='Year')
    codefor=models.CharField(max_length=30, choices=code_type,null=True,verbose_name='Code of Conduct for')
    policydoc=models.FileField(upload_to="files", verbose_name="Policy Document")
    photo=models.ImageField(upload_to='images',verbose_name=' Supporting Photos with Geo-tagg')


#Notifications
class notification_model(models.Model):
    message=models.TextField(verbose_name="Message")
    date=models.DateField(auto_now_add=True,verbose_name="Date")
    
#member
class member_model(models.Model):
    username=models.CharField(max_length=50,verbose_name="Username",primary_key=True)
    password=models.CharField(max_length=50,verbose_name="Password")