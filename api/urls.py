from django.urls import path
from .views import *
from .views_Sardor import *


urlpatterns = [
    path('ads/', AboutView.as_view({'get': 'list'})),
    path('category/', CategoryView.as_view({'get': 'list'})),
    path('subcategory/', SubcategoryView.as_view({'get': 'list'})),
]