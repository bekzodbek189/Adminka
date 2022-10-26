from django.urls import path
from .views import *


urlpatterns = [
    path('dashboart', Dashboart, name='dashboart'),
    path('sign-up/', Sing_up, name='sign-up'),
    path('', Sing_in, name='sign-in'),
    path('dashboart/', Dashboart, name='dashboart'),
    path('logout/', Logout, name='logout'),
    path('update/', UpdateUser, name='update'),
    path('profile/', Profile, name='profile')
]