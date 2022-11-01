from rest_framework.serializers import ModelSerializer
from main.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"


class AddimageSerializer(ModelSerializer):
    class Meta:
        model = AdImage
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class AdsSerializer(ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"



class ReklamaSerializer(ModelSerializer):
    class Meta:
        model = Reklama
        fields = "__all__"


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


