from django.db import models

class user_model(models.Model):
    yr_choice=[
        ('Iyr', 'First Year'),
        ('IIyr', 'Second Year'),
        ('IIIyr', 'Third Year'),
        
    ]
    sem_choice=[
        ('ISem', 'First Semester'),
        ('IISem', 'Second Semester'),
        ('IIISem', 'Third Semester'),
        ('IVSem', 'Fourth Semester'),
        ('VSem', 'Fifth Semester'),
        ('VISem', 'sixth Semester'),
    ]
    stream_choice=[
        ('BSc', 'BSc'),
        ('BCOM', 'BCOM'),
        ('BA', 'BA'),
    ]
    name=models.CharField(max_length=100,verbose_name="Name")
    email=models.EmailField(verbose_name="Email")
    phone_no=models.CharField(max_length=10,verbose_name="Phone Number")
    year=models.CharField(max_length=20,verbose_name="Year",choices=yr_choice,null=True,blank=True)
    sem=models.CharField(max_length=20,verbose_name="Semester",choices=sem_choice,null=True,blank=True)
    stream=models.CharField(max_length=20,verbose_name="Stream",choices=stream_choice,null=True,blank=True)
    comb=models.CharField(max_length=10,verbose_name="Combination/Department")
    sec=models.CharField(max_length=2,verbose_name="Section",null=True,blank=True)
    username=models.CharField(max_length=100,verbose_name="Username",primary_key=True)
    password=models.CharField(max_length=100,verbose_name="Password")
    verified=models.BooleanField(verbose_name="Is verified",default=False)
    is_conviner=models.BooleanField(verbose_name="Is_Conviner",default=False)
    def __str__(self):
        return self.username
    
class ABC(models.Model):

    CHOICES =(
    ("ARTICLE", "ARCTICLE"),
    ("SPECIAL ACHIEVEMENT", "SPECIAL ACHIEVEMENT"),
    ("REPORT OF AN EVENT", "REPORT OF AN EVENT"),
    ("ART WORK", "ART WORK"),("ANY OTHER", "ANY OTHER"),
)
    name = models.ForeignKey(
        user_model,
        on_delete=models.CASCADE, null=True,blank=True
    )
    date_and_time=models.DateTimeField(verbose_name='Date and Time', auto_now_add=True, null=True)
    title = models.CharField(max_length=30)
    doc_type = models.CharField(max_length=30, choices=CHOICES)
    doc = models.FileField(upload_to="doc")
    remarks=models.TextField(verbose_name="Remarks",null=True,blank=True)
    is_approved=models.BooleanField(verbose_name="Approved",default=False)
    def __str__(self):
        return self.title
    

# class BCA(AbstractUser):
#     is_Teacher = models.BooleanField(default=False)
#     is_Student = models.BooleanField(default=False)