from django.db import models

# Create your models here.
#member
class member_model(models.Model):
    org=models.CharField(max_length=50,verbose_name="Organisation",primary_key=True)
    password=models.CharField(max_length=50,verbose_name="Password")
    def __str__(self):
        return self.org
# cell Event planning
class cellEventplan_model(models.Model):
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
    Noofstd=models.CharField(max_length=200,  null=True,verbose_name='Number of Students attending the Event')
    Remarks=models.CharField(max_length=200,  null=True,verbose_name='Remarks')
    org=models.ForeignKey(member_model,on_delete=models.CASCADE,null="True",blank="True")


# 2 Minutes of meeting of CELL Members
class MOM_model(models.Model):
    date=models.DateField(verbose_name='Date conducted')
    mom=models.FileField(upload_to="files",verbose_name="Minutes of meeting")
    ATR=models.FileField(upload_to="files",verbose_name="Action taken Report")
    org=models.ForeignKey(member_model,on_delete=models.CASCADE,null="True",blank="True")

#5 EVENTS Conducted by the cell 


class ClubEvent_model(models.Model):
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
        ('National', 'National'),
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
    Guest=models.CharField(max_length=30,verbose_name='Guest Name')
    Guest_det=models.FileField(upload_to="files", verbose_name="Event guest Profile")
    noofstd=models.CharField(max_length=10,verbose_name='Number of Students Participated',null=True)
    atdlist=models.FileField(upload_to="files", verbose_name="Upload Student attendance",null=True)
    org=models.ForeignKey(member_model,on_delete=models.CASCADE,null="True",blank="True")
    
