from django.shortcuts import render,redirect
from django.db.models.fields.reverse_related import ManyToOneRel
from IQAC.models import member_model as iqac_member
from dept.models import dept as dept_member
from Collegecells.models import member_model as cell_member
from staff.models import profile_model as staff_member
from IQAC.forms import memberform as iqac_form
from dept.forms import memberform as dept_form
from Collegecells.forms import memberform as cell_form
from staff.forms import profileForm as staff_form

# Create your views here.
titles={
    "iqac":"IQAC member",
    "dept":"Departments",
    "cell":"Cells/Clubs",
    "staff":"Staffs",
}
def home(request):
    
    return render(request,"welcome.html")

def admin(request):
    return render(request,"admin_dashboard.html",{"titles":titles})

def disp(request,name):
    
    request.session['model']=name
    fields=eval("".join((name,"_member._meta.get_fields()")))
    field_name=[]
    for field in fields:
        if not isinstance(field, ManyToOneRel):
            field_name.append(field.verbose_name)
    
    
    data=eval("".join((name,"_member.objects.values_list().order_by('pk')")))
    pk=eval("".join((name,"_member.objects.values_list('pk')")))
    data=zip(data,pk)
    if "form" in request.POST:
        form=eval("".join((name,"_form(request.POST,request.FILES or None)")))
        
        if form.is_valid():
            form.save()
            
            form=eval("".join((name,"_form()")))
            return redirect(disp,name=name)
    else:
        
        form=eval("".join((name,"_form()")))
    
    context={
        
        'field_name':field_name,
        'title':titles[name],
        'data':data,
        "titles":titles,
        "form":form,
        "pk":pk
        }
    
    return render(request,"admin_disp.html",context)






def edit_member(request, pk):
    name=request.session['model']
    model="".join((name,"_member"))
    form_name="".join((name,"_form"))
    data = eval("".join((model,".objects.get(pk=pk)")))       
    form = eval("".join((form_name,"(instance=data)")))   
    if request.method == "POST":
        form = eval("".join((form_name,"(request.POST,request.FILES)")))
        if form.is_valid():
            form.save()
            data.delete()
            return redirect(disp ,name=name)

    context = {
        "form": form,
        "pk":pk
    }
    return render(request, "edit.html", context)




def delete_member(request, pk):
    name=request.session['model']
    model="".join((name,"_member"))
    data = eval("".join((model,".objects.get(pk=pk)"))) 
    data.delete()               
    return redirect(disp ,name=name)