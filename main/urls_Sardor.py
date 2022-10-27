from django.urls import path
from .views_Sardor import *

urlpatterns = [
    path('information/', information, name='information'),
    path('add_info/', Add_info, name='add_info'),
    path('delete_info/<int:pk>/', delete_info, name='delete_info'),
    path('change_info/<int:pk>/', change_info, name='change_info'),
    path('region/', region, name='region'),
    path('add_reg/', add_reg, name='add_reg'),
    path('delete_reg/<int:pk>/', delete_reg, name='delete_reg'),
    path('change_reg/<int:pk>/', change_reg, name='change_reg')

]