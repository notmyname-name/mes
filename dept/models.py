
from django.db import models

# Create your models here.
class faculty(models.Model):
    faculty=models.CharField(max_length=100,verbose_name="Faculty",primary_key=True)
    def __str__(self):
        return self.faculty

class dept(models.Model):
    faculty=models.ForeignKey(faculty,on_delete=models.CASCADE,verbose_name="Faculty")
    dept=models.CharField(max_length=100,verbose_name="Department",primary_key=True)
    dept_code=models.CharField(max_length=100,verbose_name='Dept Code')
    def __str__(self):
        return self.dept

#1 subject entry taught in the Department

class subject_model(models.Model):
    
    clas_choice=[
        ('ISem', 'First Semester'),
        ('IISem', 'Second Semester'),
        ('IIISem', 'Third Semester'),
        ('IVSem', 'Fourth Semester'),
        ('VSem', 'Fifth Semester'),
        ('VISem', 'sixth Semester'),
    ]
    yr_choice=[
        ('Iyr', 'First Year'),
        ('IIyr', 'Second Year'),
        ('IIIyr', 'Third Year'),
        
    ]
    year=models.CharField(max_length=8, choices=yr_choice, null=True,verbose_name='Year')
    clas = models.CharField(max_length=8, choices=clas_choice, null=True,verbose_name='Semester')
   
    titlesubject=models.CharField(max_length=100,verbose_name='Subject Name')
    tot_no_hrs=models.CharField(max_length=10,verbose_name=' Allotted Tot_no_hrs')
    dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")



    


#2 WORKLOAD ENTRY OF THE DEPARTMENT


class workld_model(models.Model):
    
    clas_choice=[
        ('ISem', 'First Semester'),
        ('IISem', 'Second Semester'),
        ('IIISem', 'Third Semester'),
        ('IVSem', 'Fourth Semester'),
        ('VSem', 'Fifth Semester'),
        ('VISem', 'sixth Semester'),
    ]
    yr_choice=[
        ('Iyr', 'First Year'),
        ('IIyr', 'Second Year'),
        ('IIIyr', 'Third Year'),
        
    ]
    year=models.CharField(max_length=8, choices=yr_choice, null=True,verbose_name='Year')
    clas = models.CharField(max_length=8, choices=clas_choice, null=True,verbose_name='Semester')
    theory_workld=models.IntegerField(verbose_name='Theory Workload',default='No Practicals')
    pract_workld=models.IntegerField(verbose_name='Practical Workload',default="no Practicles")
    dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")



#3 STUDENT STRENGTH ENTRY OF THE DEPARTMENT


class stdstrength_model(models.Model):
    
    clas_choice=[
        ('ISem', 'First Semester'),
        ('IISem', 'Second Semester'),
        ('IIISem', 'Third Semester'),
        ('IVSem', 'Fourth Semester'),
        ('VSem', 'Fifth Semester'),
        ('VISem', 'sixth Semester'),
    ]
    yr_choice=[
        ('Iyr', 'First Year'),
        ('IIyr', 'Second Year'),
        ('IIIyr', 'Third Year'),
        
    ]
    year=models.CharField(max_length=8, choices=yr_choice, null=True,verbose_name='Year')
    clas = models.CharField(max_length=8, choices=clas_choice, null=True,verbose_name='Semester')
    no_of_stud=models.IntegerField(verbose_name='No. of Students')
    combination=models.CharField(max_length=5,verbose_name="Combination")
    dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")



#4 STUDENT ACHIEVEMENT ENTRY - DEPARTMENTWISE(internship, cultural, sports, nss,ncc,rotract,redcross etc)


class stdperform_model(models.Model):
    
    clas_choice=[
        ('ISem', 'First Semester'),
        ('IISem', 'Second Semester'),
        ('IIISem', 'Third Semester'),
        ('IVSem', 'Fourth Semester'),
        ('VSem', 'Fifth Semester'),
        ('VISem', 'sixth Semester'),
    ]
    yr_choice=[
        ('Iyr', 'First Year'),
        ('IIyr', 'Second Year'),
        ('IIIyr', 'Third Year'),
        
    ]
    ty_choice=[
        ('acad', 'Academic Performance'),
        ('non-acad', 'Non-Academic Performance'),
        
        
    ]
    category=models.CharField(max_length=30, choices=ty_choice, null=True,verbose_name='Category type')
    year=models.CharField(max_length=8, choices=yr_choice, null=True,verbose_name='Year')
    clas = models.CharField(max_length=8, choices=clas_choice, null=True,verbose_name='Semester')
    combination=models.CharField(max_length=5,verbose_name="Combination")
    name=models.CharField(max_length=100,verbose_name='Name of the Student')
    email=models.EmailField(verbose_name='Email ID')
    phnum=models.CharField(max_length=100,verbose_name='Phone Number')
    event_title=models.CharField( max_length=100,verbose_name='Title of the Event')
    event_details=models.CharField( max_length=100,verbose_name='Event details',null="True",blank="True")
    certif=models.FileField(upload_to="files", verbose_name="Event Certificate")
    dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")





# 5 STUDENT PROGRESSION ENTRY - DEPARTMENTWISE(UG TO PG OR FURTHER STUDIES)


class stdprogress_model(models.Model):
      
    year=models.DateField(verbose_name='Year Studied')
    name=models.CharField(max_length=100,verbose_name='Name of the Student')
    email=models.EmailField(verbose_name='Email ID')
    phnum=models.CharField(max_length=100,verbose_name='Phone Number')
    joinedto=models.CharField(max_length=100,verbose_name='Name of the College joined to')
    coursename=models.CharField(max_length=100,verbose_name='Name of the  Course')
    dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")


#6 STUDENT PLACEMENT ENTRY - DEPARTMENTWISE


class stdplacement_model(models.Model):
      
    year=models.DateField(verbose_name='Year Studied')
    name=models.CharField(max_length=100,verbose_name='Name of the Student')
    email=models.EmailField(verbose_name='Email ID')
    phnum=models.CharField(max_length=100,verbose_name='Phone Number')
    joinedto=models.CharField(max_length=100,verbose_name='Name of the company joined to')
    paypack=models.CharField(max_length=100,verbose_name='Pay package offered')
    offer_letter=models.FileField(upload_to="files", verbose_name="Offer letter")
    dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")



#7 EVENTS OF DEPARTMENT ENTRY - DEPARTMENTWISE


class deptEvent_model(models.Model):
    ty1_choice=[
        #('click','enter')
        ('std', 'For Students'),
        ('staff', 'For Staff'),
            
        
    ]
    type_choice=[
        
        ('FDP', 'Faculty Development Program'),
        ('GL', 'Guest Lecture'),
        ('CONF', 'Conference'),
        ('WORKSP', 'workshop'),
        ('SEMINAR', 'seminar'),
        ('HANDON', 'Hands on'),
        ('WEBINAR', 'webinar'),
               
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
    conduct_for=models.CharField(max_length=30, choices=ty1_choice, null=True ,verbose_name='Event Conducted for')
    scope=models.CharField(max_length=30, choices=scope_choice,null=True,verbose_name='Type/Scope of the Event')
    category=models.CharField(max_length=30, choices=type_choice, null=True,verbose_name='Event category')
    mode=models.CharField(max_length=30, choices=m_choice, null=True,verbose_name='Mode of conducting Event')
    year=models.DateField(verbose_name='Date conducted')
    event_Title=models.CharField(max_length=100,verbose_name='Title of the Event')
    event_bro=models.FileField(upload_to="files", verbose_name="Brouchure")
    event_sche=models.FileField(upload_to="files", verbose_name="Event Schedule")
    event_Rpt=models.FileField(upload_to="files", verbose_name="Event Report")
    event_photo=models.FileField(upload_to="files", verbose_name="Event Photos")
    event_cert=models.FileField(upload_to="files", verbose_name="Event Sample Certificate")
    event_approval=models.FileField(upload_to="files", verbose_name="Event Approval/Statuory letter")
    event_misc=models.FileField(upload_to="files", verbose_name="Event Miscellaneous")
    dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")



    # 8 DEPARTMENT MEETINGS ENTRY 
class deptmeeting_model(models.Model):
     type_choice=[
        
        ('staff_meet', 'Staff Meeting'),
        ('DAC', 'Department Advisory meeting'),
        ('AAA','Academic Audit meeting'),
        ('std_meet','staff Student Meeting'),
                   
     ]
     category=models.CharField(max_length=30, choices=type_choice, null=True,verbose_name='Meeting category')
     year=models.DateField(verbose_name='Date conducted')
     agenda=models.CharField(max_length=100,verbose_name='Agenda of the Meeting')
     mom=models.FileField(upload_to="files", verbose_name='Minutes of Meeting')
     atr=models.FileField(upload_to="files", verbose_name='Action Taken Report')
     dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")



# 9 DEPARTMENT PROJECT PROPOSAL ENTRY 
class deptproposal_model(models.Model):
     type_choice=[
        
        ('Govt', 'Govenrnment'),
        ('NonGovt', 'Non-Government'),
                   
     ]
     category=models.CharField(max_length=30, choices=type_choice, null=True,verbose_name='Type of Agency')
     year=models.DateField(verbose_name='Date Applied')
     project_title=models.CharField(max_length=100,verbose_name='Title of the Project')
     agency_name=models.CharField(max_length=100,verbose_name='Name of the Agency')
     amount=models.CharField(max_length=100,verbose_name='Amount of the Project')
     circular=models.FileField(upload_to="files", verbose_name='Advertised Circular upload')
     proposal=models.FileField(upload_to="files", verbose_name='Proposal Document Upload')
     dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")

# 10 STUDENT PROJECT  ENTRY(CURRIULUM MANDATED) - DEPARTMENTWISE 
class studprj_model(models.Model):
     
     year=models.DateField(verbose_name='Project year/Date')
     project_title=models.CharField(max_length=100,verbose_name='Title of the Project')
     no_of_std=models.CharField(max_length=3,verbose_name='No. of Students in the group')
     name_of_std=models.CharField(max_length=100,verbose_name='Names of the Students')
     remarks=models.CharField(max_length=100,verbose_name='Any Remarks')
     synopsis=models.FileField(upload_to="files", verbose_name='Synopsis upload')
     dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")

# 10 DEPARTMENT COMMUNICATION FOR INTERNAL/EXTERNAL GROUP ENTRY 
class deptcomm_model(models.Model):
     type_choice=[
        
        ('Mgt', 'Management'),
        ('prin', 'Head of Institution'),
        ('staff',"Among staff"),
        ('Univ','University'),
        ('IQAC', 'IQAC')
                   
     ]
     comm_to=models.CharField(max_length=30, choices=type_choice, null=True,verbose_name='Communication type')
     year=models.DateField(verbose_name='Date Communicated')
     subject_title=models.CharField(max_length=100,verbose_name='Subject of the Communication')
     letter=models.FileField(upload_to="files", verbose_name='Sent letter upload')
     remark=models.CharField(max_length=100,verbose_name='Remark - follow up of the Communication')
     dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")
     


# 11 DEPARTMENT IMAGE GALLERY
class deptimges_model(models.Model):
    event_det=models.CharField(max_length=100,verbose_name='Details of the photo',null=False)
    date=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='images',verbose_name='Photos')
    dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")

#form set

# 11 DEPARTMENT E-RESOURCES ENTRY
class depteresource_model(models.Model):
    clas_choice=[
        ('ISem', 'First Semester'),
        ('IISem', 'Second Semester'),
        ('IIISem', 'Third Semester'),
        ('IVSem', 'Fourth Semester'),
        ('VSem', 'Fifth Semester'),
        ('VISem', 'sixth Semester'),
    ]
    yr_choice=[
        ('Iyr', 'First Year'),
        ('IIyr', 'Second Year'),
        ('IIIyr', 'Third Year'),
        
    ]
    year=models.CharField(max_length=8, choices=yr_choice,null=True,verbose_name='Year')
    clas = models.CharField(max_length=8, choices=clas_choice, null=True,verbose_name='Semester')
    date=models.DateTimeField(auto_now_add=True)


 #   sub_title = models.ForeignKey(Subject_model, on_delete=models.CASCADE)#use of many-to-one


    pract_manual=models.FileField(upload_to="files",verbose_name='Practical Manual')
    e_book=models.FileField(upload_to="files",verbose_name='E-Book')# how to upload many E-books for same subject
    video=models.FileField(upload_to="files", verbose_name="Video Link" ,blank=True)
    qp=models.FileField(upload_to="files", verbose_name="Question Paper")
    solvedQP=models.FileField(upload_to="files", verbose_name="Solved Question Paper")
    study_mat=models.FileField(upload_to="files", verbose_name="Department Notes")
    others=models.FileField(upload_to="files", verbose_name="Any other relevant material")
    dept=models.ForeignKey(dept,on_delete=models.CASCADE,null="True",blank="True")





