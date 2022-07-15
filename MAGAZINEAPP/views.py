from os import remove
from typing import Type
from django.http import request
from django.shortcuts import render, redirect,HttpResponse
from MAGAZINEAPP.forms import *
import MAGAZINEAPP.models as md
from PyPDF2 import PdfFileMerger
from .filters import SearchFilter
from django.core.paginator import Paginator



def main_view(request):
    return render(request, "MAGAZINEAPP/templates/main.html")



def login_view(request):
    if request.method == "POST":
        form = LoginPage(request.POST or None)
        if form.is_valid():
            user_exist=md.user_model.objects.filter(username=str(form.cleaned_data['Username']),password=str(form.cleaned_data['password'])).first()
            if user_exist:
                if user_exist.verified:
                    return redirect('MAGAZINEAPP_display',username=user_exist.username)
                else:
                    return render(request, "/MAGAZINEAPP/templates/login.html",{"message":"Your acount is not verified yet"})
    else:
        form = LoginPage()

    context = {
        "form": form
    }
    
    return render(request, "MAGAZINEAPP/templates/login.html", context)


def register_view(request):
    if request.method == "POST":
        form = user_FORM(request.POST or None)
        if form.is_valid():
            
            form.save()
            if form.cleaned_data['verified']:
                username=str(form.cleaned_data['username'])
                return redirect('MAGAZINEAPP_display',username=username)
            
            else:
                return redirect('MAGAZINEAPP_login')
                
    else:
        form = user_FORM()
    context = {
        "form": form
    }
    return render(request, "MAGAZINEAPP/templates/register.html", context)



def logout_view(request):
    return redirect("/")

def magazine_form_view(request,username):
    if request.method == "POST":
        form = MagazineForm(request.POST,request.FILES or None)
        form.data._mutable = True
        form.data["name"] = username
        form.data._mutable = False
        if form.is_valid():
            form.save()
            form = MagazineForm()
            return redirect('MAGAZINEAPP_display',username=username)

    else:
        form = MagazineForm()
        
    context = {
        "form": form,
        "username":username
    }
    return render(request, "MAGAZINEAPP/templates/magazine_form.html", context)



def display_view(request,username):
    context = {}
    user=md.user_model.objects.get(pk=username)
    if user.is_conviner:
        searchfilter = SearchFilter(request.GET, queryset=ABC.objects.all())
        user_list=md.user_model.objects.all()
    else:
        searchfilter = SearchFilter(request.GET, queryset=ABC.objects.filter(name=username))
        user_list=None
    file="~".join([str(i) for i in list(searchfilter.qs.values_list("id", flat=True))])
    if not file:
        file='none'
    p = Paginator(searchfilter.qs, 10)
    page = request.GET.get('page')
    pagination = p.get_page(page)
    
    context = {
        "search": searchfilter,
        "pagination": pagination,
        "username":username,
        "user_list":user_list,
        "file":file
    }
    return render(request, "MAGAZINEAPP/templates/display.html", context = context)

def merge_download(request,file):
    if file is "none":
        return
    merger = PdfFileMerger()
    file=file.split('~')
    for pdf in file:
        merger.append(ABC.objects.get(id=pdf).doc )

    merger.write("result.pdf")
    response = HttpResponse(open("result.pdf","rb").read(),content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename=some_file.pdf'
    merger.close()
    remove("result.pdf")
    return response
   
    

def edit_view(request, pk,username):
    data = ABC.objects.get(id=pk)  
    if user_model.objects.get(pk=username).is_conviner:
        form = ConvinerMagazineForm(instance=data)     
        if request.method == "POST":
            form =ConvinerMagazineForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect('MAGAZINEAPP_display',username=username)
    else:
        form = MagazineForm(instance=data)     
        if request.method == "POST":
            form = MagazineForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect('MAGAZINEAPP_display',username=username)

    context = {
        "form": form
    }
    return render(request, "MAGAZINEAPP/templates/edit.html", context)




def delete_view(request, pk,username):
    
    data = ABC.objects.get(id=pk)
    if request.method == "POST":
        data.delete()                 #DELETES THE DATA
        return redirect('MAGAZINEAPP_display',username=username)
    context = {
        "item": data,
        "username":username
    }
    return render(request, "MAGAZINEAPP/templates/delete.html", context)


def user_verification(request,user,username):
    
    user = user_model.objects.get(pk=user)
    form = verify_FORM(instance=user)
    if request.method == "POST":
        form = verify_FORM(request.POST, instance=user)
        if form.is_valid():
            
            if form.cleaned_data['verified']:
                if not user.verified:
                    pass
                
                if form.cleaned_data['is_conviner']:
                    if not user.is_conviner:
                        pass
                    conviner=user_model.objects.get(pk=username)
                    conviner.is_conviner=False
                    conviner.save()
                form.save()
            else:
                user.delete()
            
            
            return redirect('MAGAZINEAPP_display',username=username)

    context = {
        "form": form
    }
    
    return render(request,"MAGAZINEAPP/templates/verification.html", context)