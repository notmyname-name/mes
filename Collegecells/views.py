from django.shortcuts import render,redirect
from django.core.paginator import Paginator
import Collegecells.models as md 
from Collegecells.forms import *
from Collegecells.filters import *
from django.http import HttpResponseRedirect

# Create your views here.


titles={
    "cellEventplan":"Cell Event planning",
    "MOM":"Minutes of meeting",
    "ClubEvent":"EVENTS Conducted",
}

def home(request):
    
    return render(request,"cell/cell_dashboard.html",{"titles":titles})

def cell_display(request,name,title):
    request.session['name']=name
    request.session['title']=title
    model="".join((name,"_model"))
    filter="".join((name,"_Filter"))
    fields=eval("".join(("md.",model,"._meta.get_fields()")))
    
    field_name=[field.verbose_name for field in fields]
    field_name.remove('ID')
    
    searchfilter = eval("".join((filter,"(request.GET, queryset=",model,".objects.values_list().filter(org=request.session['org']))")))
    p = Paginator(searchfilter.qs, 10)
    page = request.GET.get('page')
    pagination = p.get_page(page)
    if "form" in request.POST:
        form=eval("".join((name,"form(request.session['org'],request.POST,request.FILES or None)")))
        
        if form.is_valid():
            form.save()
            
            form=eval("".join((name,"form(request.session['org'])")))
            return redirect(cell_display,name=name,title=title)
    else:
        
        form=eval("".join((name,"form(request.session['org'])"))) 
    
    context={
        'field_name':field_name,
        'titles':titles,
        'title':title,
        'name':name,
        "search": searchfilter,
        "pagination": pagination,
        "form":form,
        }
    return render(request,'cell/cell_disp.html',context)



def edit_cell(request, pk):
    
    name=request.session['name']
    title= request.session['title']  
       
    model="".join((name,"_model"))
    form_name="".join((name,"form"))
    data = eval("".join((model,".objects.get(id=pk)")))       
    form = eval("".join((form_name,"(request.session['org'],instance=data)"))) 
    
    if request.method == "POST":
        form = eval("".join((form_name,"(request.session['org'],request.POST,request.FILES,instance=data)")))
        print(form.is_valid())  
        if form.is_valid():
            form.save()
            return redirect(cell_display,name=name,title=title)

    context = {
        "form": form,
        "pk":pk
    }
    return render(request, "cell/edit.html", context)




def delete_cell(request, pk):
    name=request.session['name']
    title= request.session['title'] 
    model="".join((name,"_model"))
    data = eval("".join((model,".objects.get(id=pk)"))) 
    
    data.delete()                 
    return redirect(cell_display,name=name,title=title)
    

def login(request):
    details=md.member_model.objects.values_list('org','password')
    
    if request.method=='POST':
        form=LoginPage(request.POST or None)
        
        if form.is_valid():
            dept = str(form.cleaned_data['Username'])
            password = str(form.cleaned_data['Password'])
            
            for i in details:
                if dept==i[0] and password==i[1]:
                    
                    request.session['org']=dept
                    
                    
                        
                        
                    return home(request)
                    
            form=LoginPage()
            return HttpResponseRedirect('/cell//')
    else:
        form=LoginPage() 
    return render(request,"cell/form.html",{'form':form,'title':"Login",})