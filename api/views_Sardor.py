from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
import django_filters.rest_framework
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from main.models import *
from .serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class AdsView(generics.ListAPIView):
    queryset = Ads.objects.all()
    safety_regulations = AdsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'category', 'category__subcategory']
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category', 'category__subcategory', 'price', 'region' ]
    pagination_class = StandardResultsSetPagination



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



