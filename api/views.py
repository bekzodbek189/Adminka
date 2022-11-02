from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
import django_filters.rest_framework

from main.models import *
from .serializers import *


class InformationView(ReadOnlyModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


class AboutView(ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer



class ReklamaView(ReadOnlyModelViewSet):
    queryset = Reklama.objects.all()
    serializer_class = ReklamaSerializer


