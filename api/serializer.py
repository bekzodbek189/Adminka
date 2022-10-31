from rest_framework import serializers
from main.models import *


class Informations_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'
        
class AdImage_serializer(serializers.ModelSerializer):
    class Meta:
        model = AdImage
        fields = '__all__'
        
class District_Serializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
        
class Region_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'





class Subcategory_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'



class ADS_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'



class Reklama_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reklama
        fields = '__all__'






class About_Serializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


















        
