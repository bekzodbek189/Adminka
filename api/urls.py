from rest_framework.routers import DefaultRouter
from api import views
from django.urls import path, include




router = DefaultRouter()
router.register(r'inform', views.InformationView, basename="inform")
router.register(r'about', views.AboutView, basename="about")
router.register(r'reklama', views.ReklamaView, basename="reklama")
router.register(r'privacy', views.Privacy_policyView, basename="privacy")
router.register(r'theme', views.ThemeView, basename="theme")
router.register(r'safety', views.Safety_regulationsView, basename="safety")
router.register(r'sale_buy', views.How_to_sale_and_buyView, basename="sale_buy")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
