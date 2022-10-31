from rest_framework.routers import DefaultRouter
from api import views
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

scheme_view = get_schema_view(
    openapi.Info(
        title=' OLX Api',
        default_version='v1',
        description='best of the best',

    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)




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
    path('swagger/ui/', scheme_view.with_ui('swagger', cache_timeout=0), name='scheme-swagger-ui')

]
