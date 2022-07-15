
from django.urls import path
from Collegecells.views import *

urlpatterns = [
    path('/',login,name='cell_login'),
    path('home/',home,name='cell_home'),
    
    path('cell_display/<str:name>,<str:title>/', cell_display,name='cell_display'),
    path('edit_cell/<str:pk>/', edit_cell,name='edit_cell'),
    path('delete_cell/<str:pk>/', delete_cell,name='delete_cell'),
   
    
]
