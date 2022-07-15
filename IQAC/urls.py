
from django.urls import path
from IQAC.views import *

urlpatterns = [
    path('/',login,name='IQAC_login'),
    path('home/',home,name='IQAC_home'),
    path('iqac_display/<str:name>,<str:title>/', iqac_display,name='iqac_display'),
    path('edit/<str:pk>/', edit_iqac,name='edit_iqac'),
    path('delete/<str:pk>/', delete_iqac,name='delete_iqac'),
    path('send_email/', send_email,name="send_email"),
    path('notify_display/', notify_display,name="notify_display"),
    
]
