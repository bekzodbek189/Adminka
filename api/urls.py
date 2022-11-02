from django.urls import path
from .views import *
from .views_Sardor import *


urlpatterns = [
    path('ads/', AdsView.as_view()),
    path('category/', CategoryView.as_view()),
    path('subcategory/', SubcategoryView.as_view()),
]