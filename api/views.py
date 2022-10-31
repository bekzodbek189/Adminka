from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

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


class AdsView(generics.ListCreateAPIView):
    queryset = Ads.objects.all()
    safety_regulations = AdsSerializer


class AdsChangeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ads.objects.all()
    safety_regulations = AdsSerializer


class AdsImageView(generics.ListCreateAPIView):
    queryset = AdImage.objects.all()
    safety_regulations = AddimageSerializer



class AdsImageChangeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdImage.objects.all()
    safety_regulations = AddimageSerializer

