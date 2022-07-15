"""MAGAZINE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from MAGAZINEAPP.views import *

urlpatterns = [
    
    path("", main_view, name="main"),
    path("login/", login_view, name="MAGAZINEAPP_login"),
    path('register/', register_view, name="register"),
    path('magazine/<str:username>', magazine_form_view, name="magazine"),
    path('logout/', logout_view, name="logout"),
    path('display/<str:username>', display_view, name="MAGAZINEAPP_display"),
    path('merge_download/<str:file>', merge_download, name="merge_download"),
    path('user_verification/<str:user>,<str:username>', user_verification, name="user_verification"),
    path('edit/<str:pk>,<str:username>/', edit_view, name="edit"),
    path('delete/<str:pk>,<str:username>/', delete_view, name="delete"),
]
