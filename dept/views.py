from django.shortcuts import render,redirect
from dept.forms import *
from django.core.paginator import Paginator
import dept.models as md 
from django.http import HttpResponseRedirect
from dept.filters import *

# Create your views here.

titles={
    "subject":"Subject",
    "workld":"Work Load",
    "stdstrength":"Student Strength",
    "stdperform":"Student Performance",
    "stdprogress":"Student Progression",
    "stdplacement":"Student Placement",
    "deptEvent":"Events of Department",
    "deptmeeting":"Department Meeting",
    "deptproposal":"Department Project Proposal",
    "deptcomm":"Department Communication For Internal or External Group",
    "deptimges":"Department Image Gallery",
    "depteresource":"Department E-Resources"
}


def home(request):
    
    return render(request,"dept/dept_dashboard.html",{"dept":request.session['dept'],"titles":titles,"design":request.session['design']})

def dept_display(request,name,title):
    request.session['name']=name
    request.session['title']=title
    model="".join((name,"_model"))
    filter="".join((name,"_Filter"))
    fields=eval("".join(("md.",model,"._meta.get_fields()")))
    field_name=[field.verbose_name for field in fields]
    field_name.remove('ID')
    searchfilter = eval("".join((filter,"(request.GET, queryset=",model,".objects.filter(dept=request.session['dept']).values_list())")))
    p = Paginator(searchfilter.qs, 10)
    page = request.GET.get('page')
    pagination = p.get_page(page)
    if "form" in request.POST:
        form=eval("".join((name,"form(request.session['dept'],request.POST,request.FILES or None)")))
        
        if form.is_valid():
            form.save()
            
            form=eval("".join((name,"form(request.session['dept'])")))
            return redirect(dept_display,name=name,title=title)
    else:
        
        form=eval("".join((name,"form(request.session['dept'])"))) 
    
    context={
        "dept":request.session['dept'],
        'field_name':field_name,
        'title':title,
        'titles':titles,
        'name':name,
        "search": searchfilter,
        "pagination": pagination,
        "form":form,
        }
    return render(request,'dept/dept_disp.html',context)
    

# 
def edit_dept(request, pk):
    name=request.session['name']
    title= request.session['title']
    model="".join((name,"_model"))
    form_name="".join((name,"form"))
    data = eval("".join((model,".objects.get(id=pk)")))       
    form = eval("".join((form_name,"(request.session['dept'],instance=data)")))   
    if request.method == "POST":
        form = eval("".join((form_name,"(request.session['dept'],request.POST,request.FILES,instance=data)")))
        if form.is_valid():
            form.save()
            return redirect(dept_display,name=name,title=title)

    context = {
        "form": form,
        "pk":pk
    }
    return render(request, "dept/edit.html", context)




def delete_dept(request, pk):
    name=request.session['name']
    title= request.session['title'] 
    model="".join((name,"_model"))
    data = eval("".join((model,".objects.get(id=pk)"))) 
    
    data.delete()                 
    return redirect(dept_display,name=name,title=title)




# def login(request):
#     details=md.dept.objects.values_list('name','dept_code')
    
#     if request.method=='POST':
#         form=LoginPage(request.POST or None)
        
#         if form.is_valid():
#             dept = str(form.cleaned_data['Department'])
#             password = str(form.cleaned_data['password'])
            
#             for i in details:
#                 if dept==i[0] and password==i[1]:
#                     request.session['dept']=dept
                    
                    
                        
                        
#                     return render(request,"dept/dept_dashboard.html",{"dept":dept,"titles":titles})
                    
#             form=LoginPage()
#             return HttpResponseRedirect('/dept/')
#     else:
#         form=LoginPage() 
        
#     return render(request,"form.html",{'form':form,'title':details,})