from django.urls import path
from .viewset import *

urlpatterns = [
    path("user_ads/<int:pk>/", Ads_user),
    path("info/", InformationView.as_view({'get': 'list'})),
    path("user/", UserView.as_view()),
    path("add_ads/", Add_ads.as_view()),
    path("users_ads/", Users_ads),
    path("add_img", Add_img),
    path("add_ads", Add_ads)
]