from django.urls import path
from .views import *


urlpatterns = [
    path('dashboard', Dashboart, name='dashboard'),
    path('', Sing_in, name='sign_in'),
    path('logout/', Logout, name='logout'),
    path('update/', UpdateUser, name='update'),
    path('profile/', Profile, name='profile'),
    path('subcategory_add/', Subcategory_add, name='subcategory_add'),
    path('subcategorys/', Subcategoys, name='subcategorys'),
    path('sub-change/<int:pk>/', Subcategory_change, name='sub-change'),
    path('sub-delete/<int:pk>/', Sub_delete, name='sub-delete'),
    path('region-delete/<int:pk>/', Region_delete, name='region-delete'),
    path('regi-change/<int:pk>/', Region_change, name='region-change'),
    path('regions/', Regions, name='regions'),
    path('region-add/', Region_add, name='regions_add'),
    path('district-delete/<int:pk>/', District_delete, name='district-delete'),
    path('district-change/<int:pk>/', District_change, name='district-change'),
    path('districts/', Districts, name='districts'),
    path('district-add/', Distrtict_add, name='district_add'),

]