from django.urls import path
from .views import *
from .views_Sardor import *


urlpatterns = [
    path('ads/', AdsView.as_view()),
    path('category/', CategoryView.as_view()),
    path('subcategory/', SubcategoryView.as_view()),
    path('about/', AboutView.as_view({'get':'list'})),
    path('reklama/', ReklamaView.as_view({'get':'list'})),
    path('info/', InformationView.as_view({'get':'list'})),
]