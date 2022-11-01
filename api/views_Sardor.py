from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
import django_filters.rest_framework
from rest_framework import filters
from main.models import *
from .serializers import *


class AdsView(generics.ListAPIView):
    queryset = Ads.objects.all()
    safety_regulations = AdsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'category', 'category__subcategory']
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category', 'category__subcategory', 'price', 'region' ]



class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields =[ 'name', ]



class SubcategoryView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields =[ 'name', 'category', ]



