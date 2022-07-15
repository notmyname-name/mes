
from django.urls import path
from main.views import *

urlpatterns = [
    
    path('', home,name='home'),
    path('it_admin/', admin,name='admin'),
    path('disp/<str:name>/', disp,name='disp'),
    path('edit_member/<str:pk>/', edit_member,name='edit_member'),
    path('delete_member/<str:pk>/', delete_member,name='delete_member'),
]
