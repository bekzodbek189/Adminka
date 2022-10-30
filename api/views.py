from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
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



class Privacy_policyView(ReadOnlyModelViewSet):
    queryset = privacy_policy.objects.all()
    serializer_class = privacy_policySerializer



class ThemeView(ReadOnlyModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer



class Safety_regulationsView(ReadOnlyModelViewSet):
    queryset = safety_regulations.objects.all()
    serializer_class = safety_regulationsSerializer



class How_to_sale_and_buyView(ReadOnlyModelViewSet):
    queryset = how_to_sale_and_buy.objects.all()
    serializer_class = how_to_sale_and_buySerializer


