from django.forms.utils import flatatt
from django.shortcuts import render,redirect
from staff.forms import *
from staff.filters import *
from django.core.paginator import Paginator

import staff.models as md 
from dept.views import home


title={
    "aad":"Academic Attendance",
    "misc":"Miscellenious Details",
    "univ":"University Details",
    "pub":"Publications",
    "port":"Portfolio",
}

def profile(request):
    title='Staff Details'
    if request.method == 'POST':
        form=profileForm(request.POST,request.FILES or None)
        
        if form.is_valid():
            form.save()
            
            
            
            return redirect(login)
    else:
        form=profileForm()        
    
    return render(request,"form.html",{'form':form,"title":title})






def profile_display(request):
    dataset=md.profile_model.objects.filter(username=request.session['Staff']).first()
    
    return render(request,'staff/profile.html',{'data':dataset})

def staff_display(request,name,title):
    request.session['name']=name
    request.session['title']=title
    model="".join((name,"_model"))
    filter="".join((name,"_Filter"))
    fields=eval("".join(("md.",model,"._meta.get_fields()")))
    field_name=[field.verbose_name for field in fields]
    field_name.remove('ID')
    searchfilter = eval("".join((filter,"(request.GET, queryset=",model,".objects.filter(staff=request.session['Staff']).values_list())")))
    p = Paginator(searchfilter.qs, 10)
    page = request.GET.get('page')
    pagination = p.get_page(page)
    pdf=searchfilter.qs
    if "form" in request.POST:
        form=eval("".join((name,"Form(request.session['Staff'],request.POST,request.FILES or None)")))
        
        if form.is_valid():
            form.save()
            
            form=eval("".join((name,"Form(request.session['Staff'])")))
            return redirect(staff_display,name=name,title=title)
    else:
        
        form=eval("".join((name,"Form(request.session['Staff'])"))) 
    
    context={
        
        'field_name':field_name,
        'title':title,
        'name':name,
        "search": searchfilter,
        "pagination": pagination,
        "pdf":pdf,
        "form":form,
        }
    return render(request,'staff/staff_disp.html',context)
def download(request,name,title):
    
    model="".join((name,"_model"))
    filter="".join((name,"_Filter"))
    fields=eval("".join(("md.",model,"._meta.get_fields()")))
    field_name=[field.verbose_name for field in fields]
    
    
    pdf=eval("".join((model,".objects.filter(staff=request.session['Staff']).values_list()")))
    context={
        
        'field_name':field_name,
        'title':title,
        'name':name,
        
        "pdf":pdf
        }
    return render(request,'staff/download.html',context)





    
def login(request):
    
    message=''
    if request.method=='POST':
        form=LoginPage(request.POST or None)
        
        if form.is_valid():
            username = str(form.cleaned_data['Username'])
            password = str(form.cleaned_data['password'])
            dept = str(form.cleaned_data['Department'])
            user_exist=md.profile_model.objects.filter(username=username,password=password,dept=dept).first()
            
            if user_exist:
                
                request.session['Staff']=user_exist.username
                request.session['design']=user_exist.designation
                request.session['dept']=dept
                return home(request)
                
                
            else:
                message='Incorrect Username or password'
            
    else:
        form=LoginPage() 
    return render(request,"staff/form.html",{'form':form,'message':message,"title":'Login'})

def staff_home(request):
    data=md.profile_model.objects.filter(username=request.session['Staff']).values('name','designation','photo')
    return render(request,"staff/staff_home.html",{"data":data[0],"title":title})
                
    
def load_branches(request):
    if request.GET.get('faculty'):
        faculty_id = request.GET.get('faculty')
        dept = md.dept.objects.filter(faculty_id=faculty_id).order_by('name')
        return render(request, 'branch_dropdown_list_options.html', {'dept': dept})
    
    


def edit_staff(request, pk):
    name=request.session['name']
    title= request.session['title']  
    model="".join((name,"_model"))
    form_name="".join((name,"Form"))
    data = eval("".join((model,".objects.get(pk=pk)"))) 
          
    form = eval("".join((form_name,"(request.session['Staff'],instance=data)")))   
    if request.method == "POST":
        form = eval("".join((form_name,"(request.session['Staff'],request.POST,request.FILES,instance=data)")))
        if form.is_valid():
            form.save()
            return redirect(staff_display ,name=name,title=title)

    context = {
        "form": form,
        "pk":pk
    }
    return render(request, "staff/edit.html", context)

def edit_profile(request, pk):
    name="profile"
      
    model="".join((name,"_model"))
    form_name="".join((name,"Form"))
    data = eval("".join((model,".objects.get(pk=pk)"))) 
          
    form = eval("".join((form_name,"(instance=data)")))  
    
    if request.method == "POST":
        
        form = eval("".join((form_name,"(request.POST,request.FILES,instance=data)")))
        
        if form.is_valid():
            
            form.save()
             
            return redirect(profile_display)

    context = {
        "form": form,
        "pk":pk
    }
    return render(request, "form.html", context)


def delete_staff(request, pk):
    name=request.session['name']
    title= request.session['title'] 
    model="".join((name,"_model"))
    data = eval("".join((model,".objects.get(id=pk)"))) 
    data.delete()                 #DELETES THE DATA
    return redirect(staff_display ,name=name,title=title)
    
    
    
def hod(request,model_download):
    
    if model_download!="none":
        name=model_download
        model="".join((name,"_model"))
        fields=eval("".join(("md.",model,"._meta.get_fields()")))
        field_name=[field.verbose_name for field in fields]
        
        
        pdf=eval("".join((model,".objects.all().values_list()")))
        context={
            
            'field_name':field_name,
            'title':title[name],
            'name':name,
            
            "pdf":pdf
            }
        return render(request,'staff/download.html',context)
    
        
    context={
        
        
        "title":title
        }
    return render(request,'staff/hod.html',context)
    

    
    
#pk.puni872@gmail.com



# def aad(request):
#     title='Staff Academic Attendance'
#     if request.method == 'POST':
#         form=aadForm(request.POST,request.FILES or None)
#         form.data._mutable = True
#         form.data["staff"] = detail['Number']
#         form.data._mutable = False
#         if form.is_valid():
            
#             form.save()
            
#             form=aadForm() 
#             return HttpResponseRedirect('/')
#     else:
#         form=aadForm()        
    
#     return render(request,"form.html",{'form':form,"title":title})
# def misc(request):
#     title='Staff Miscellenious Details'
#     if request.method == 'POST':
#         form=miscForm(request.POST,request.FILES or None)
#         form.data._mutable = True
#         form.data["staff"] = detail['Number']
#         form.data._mutable = False
#         if form.is_valid():
#             form.save()
            
#             form=miscForm() 
#             return HttpResponseRedirect('/')
#     else:
#         form=miscForm()        
    
#     return render(request,"form.html",{'form':form,"title":title})
# def univ(request):
#     title='Staff University Document Details'
#     if request.method == 'POST':
#         form=univForm(request.POST,request.FILES or None)
#         form.data._mutable = True
#         form.data["staff"] = detail['Number']
#         form.data._mutable = False
#         if form.is_valid():
#             form.save()
            
#             form=univForm() 
#             return HttpResponseRedirect('/')
#     else:
#         form=univForm()        
    
#     return render(request,"form.html",{'form':form,"title":title})

# def pub(request):
#     title='Publication of staff'
#     if request.method == 'POST':
#         form=pubForm(request.POST,request.FILES or None)
#         form.data._mutable = True
#         form.data["staff"] = detail['Number']
#         form.data._mutable = False
#         if form.is_valid():
#             form.save()
            
#             form=pubForm() 
#             return HttpResponseRedirect('/')
#     else:
#         form=pubForm()        
    
#     return render(request,"form.html",{'form':form,"title":title})


# def port(request):
#     title='Portfolio'
#     if request.method == 'POST':
#         form=portForm(request.POST,request.FILES or None)
#         form.data._mutable = True
#         form.data["staff"] = detail['Number']
#         form.data._mutable = False
#         if form.is_valid():
#             form.save()
            
#             form=portForm() 
#             return HttpResponseRedirect('/')
#     else:
#         form=portForm()        
    
#     return render(request,"form.html",{'form':form,"title":title})


# def port_disp(request):
#     fields=md.port_model._meta.get_fields()
#     field_name=[field.verbose_name for field in fields]
#     field=[field.name for field in fields]
#     field_name.remove('ID')
#     field.remove('id')
#     field_name.remove('staff')
#     field.remove('staff')
    
#     data= md.port_model.objects.filter(staff=detail['Number']).values_list(*field)
#     return render(request, 'disp_model.html', {'data': data,'field_name':field_name,})