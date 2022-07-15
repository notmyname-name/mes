
from django.urls import path
from dept.views import *
from django.urls.conf import include
import staff.urls as staff
urlpatterns = [
    
    path('home/',home,name='dept_home'),
    path('dept_display/<str:name>,<str:title>/', dept_display,name='dept_display'),
    path('edit_dept/<str:pk>/', edit_dept,name='edit_dept'),
    path('delete_dept/<str:pk>/', delete_dept,name='delete_dept'),
   
    path('staff/',include(staff)),
]
