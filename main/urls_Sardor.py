from django.urls import path
from .views_Sardor import *

urlpatterns = [
    path('information/', information, name='information')

]