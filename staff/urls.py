
from django.urls import path
from staff.views import *

urlpatterns = [
    
    
    path('profile_display/', profile_display,name='profile_display'),
   
    path('staff_display/<str:name>,<str:title>/', staff_display,name='staff_display'),
    path('download/<str:name>,<str:title>/', download,name='download'),
    path('edit/<str:pk>/', edit_staff,name='edit_staff'),
    path('edit_profile/<str:pk>/', edit_profile,name='edit_profile'),
    path('delete/<str:pk>/', delete_staff,name='delete_staff'),
    path('profile/', profile,name="profile_register"),
    
    path("staff_login",login,name="staff_login"),
    path('', staff_home,name="staff_home"),
    path('hod/<str:model_download>,', hod,name='hod'),
    path('ajax/load-branches/', load_branches, name='ajax_load_branches'),
]
