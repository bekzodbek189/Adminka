from django.urls import path
from .views_Sardor import *

urlpatterns = [
    path('information/', information, name='information'),
    path('add_info/', Add_info, name='add_info'),
    path('change_info/<str:pk>/', change_info, name='change_info')

]