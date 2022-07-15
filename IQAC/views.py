from django.shortcuts import render,redirect
from django.core.paginator import Paginator
import IQAC.models as md 
from IQAC.forms import *
from IQAC.filters import *
from django.http import HttpResponseRedirect

from staff.models import profile_model
from dept.models import dept
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


titles={
    "IQAC_COE":"CALENDER OF EVENTS",
    "Aqar":"Aqar Reports",
    "MOM":"Minutes of meeting",
    "iqacmeeting":"IQAC MEETINGS",
    "iqacEvent":"EVENTS OF IQAC",
    "IQACmandatedoc":"IQAC Mandatory or Statuory Document",
    "Actioniqac":"IQAC Action plan ",
    "Mouiqac":"IQAC MOU's",
    "Infraiqac":"IQAC Details of Infrastructure Augmentation",
    "addoncourse":"IQAC Details of Add on Courses",
    "auditRpt":"Financial Audit Report of the college",
    "CollegeauditRpt":"Other Audit Report of the college",
    "scholarshipdet":"Scholarship details",
    "Financegrants":"Funds or grants recieved from govt or non-govt or management for different purpose",
    "codeconduct":"Code of conduct",
    "notification":"Create Notifications"
}


def home(request):
    data=notification_model.objects.all()
    return render(request,"iqac/iqac_dashboard.html",{"titles":titles,"data":data})

def iqac_display(request,name,title):
    request.session['name']=name
    request.session['title']=title
    model="".join((name,"_model"))
    filter="".join((name,"_Filter"))
    fields=eval("".join(("md.",model,"._meta.get_fields()")))
    field_name=[field.verbose_name for field in fields]
    field_name.remove('ID')
    
    searchfilter = eval("".join((filter,"(request.GET, queryset=",model,".objects.values_list())")))
    p = Paginator(searchfilter.qs, 10)
    page = request.GET.get('page')
    pagination = p.get_page(page)
    if "form" in request.POST:
        form=eval("".join((name,"form(request.POST,request.FILES or None)")))
        
        if form.is_valid():
            form.save()
            
            form=eval("".join((name,"form()")))
            return redirect(iqac_display,name=name,title=title)
    else:
        
        form=eval("".join((name,"form()"))) 
    
    context={
        'field_name':field_name,
        'titles':titles,
        'title':title,
        'name':name,
        "search": searchfilter,
        "pagination": pagination,
        "form":form,
        }
    return render(request,'iqac/iqac_disp.html',context)

# def iqac_form(request,title,form_name):
    
    
#     if "form" in request.POST:
#         form=eval("".join((form_name,"form(request.POST,request.FILES or None)")))
#         # form.data._mutable = True
#         # form.data["dept"] = detail['dept']
#         # form.data._mutable = False
#         if form.is_valid():
            
                
#             form.save()
            
#             form=eval("".join((form_name,"form()")))
            
#             return redirect(iqac_display,name=form_name,title=title)
#     else:
        
#         form=eval("".join((form_name,"form()"))) 
#     return render(request,"form.html",{'form':form,"title":title})   

def edit_iqac(request, pk):
    name=request.session['name']
    title= request.session['title'] 
    model="".join((name,"_model"))
    form_name="".join((name,"form"))
    data = eval("".join((model,".objects.get(id=pk)")))       
    form = eval("".join((form_name,"(instance=data)")))   
    if request.method == "POST":
        form = eval("".join((form_name,"(request.POST,request.FILES,instance=data)")))
        if form.is_valid():
            form.save()
            return redirect(iqac_display,name=name,title=title)

    context = {
        "form": form,
        "pk":pk
    }
    return render(request, "iqac/edit.html", context)



    
        
def delete_iqac(request, pk):
    name=request.session['name']
    title= request.session['title'] 
    model="".join((name,"_model"))
    data = eval("".join((model,".objects.get(id=pk)"))) 
    
    data.delete()                 
    return redirect(iqac_display,name=name,title=title)
    


def send_email(request):
    dataset=list(dept.objects.values_list('name',flat=True).order_by('faculty'))
    dept_email={}
    for i in dataset:
        dept_email[i]=list(profile_model.objects.filter(dept=i).values_list('name','email'))
    
    if request.method=='POST':
        message = request.POST["message"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list =dict(request.POST)['mail']
        
        print(dict(request.POST)['mail'],message)
        
        form=notificationform(request.POST,request.FILES or None)
        
        if form.is_valid():
            form.save()
            send_mail( '',message, email_from, recipient_list )
    form=notificationform()
    return render(request,"iqac/send_mail.html",{'dept_email':dept_email,'form':form})

def notify_display(request):
    name='notification'
    title="Notifications"
    model="".join((name,"_model"))
    filter="".join((name,"_Filter"))
    fields=eval("".join(("md.",model,"._meta.get_fields()")))
    field_name=[field.verbose_name for field in fields]
    # field_name.remove('dept')
    searchfilter = eval("".join((filter,"(request.GET, queryset=",model,".objects.values_list())")))
    p = Paginator(searchfilter.qs, 10)
    page = request.GET.get('page')
    pagination = p.get_page(page)
    
    context={
        'field_name':field_name,
        'title':title,
        'name':name,
        "search": searchfilter,
        "pagination": pagination,
        }
    return render(request,'iqac/notify_display.html',context)

def login(request):
    details=md.member_model.objects.values_list('username','password')
    
    if request.method=='POST':
        form=LoginPage(request.POST or None)
        
        if form.is_valid():
            dept = str(form.cleaned_data['Username'])
            password = str(form.cleaned_data['Password'])
            
            for i in details:
                if dept==i[0] and password==i[1]:
                    
                    print(True)
                    
                        
                        
                    return home(request)
                    
            form=LoginPage()
            return HttpResponseRedirect('/IQAC//')
    else:
        form=LoginPage() 
    return render(request,"form.html",{'form':form,'title':"Login",})

