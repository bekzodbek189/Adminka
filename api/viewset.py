import datetime

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def Ads_user(request, pk):
    top = []
    recommended = []
    ads = []
    for i in Ads.objects.filter(owner_id=pk):
        ads.append(AdsSerializer(Ads.objects.get(id=i.id)).data)
        if i.is_top == True:
            top.append(AdsSerializer(Ads.objects.get(id=i.id)).data)
        else:
            pass
        if i.is_recommended == True:
            recommended.append(AdsSerializer(Ads.objects.get(id=i.id)).data)
        else:
            pass
    return Response({"all_ads": ads, "is top": top, "is recommended": recommended})


class InformationView(viewsets.ReadOnlyModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


class UserView(APIView):
    def get(self, request, format=None):
        users = []
        for i in User.objects.filter(status=2):
            users.append(UserSerializer(User.objects.get(id=i.id)).data)
        return Response({"Users": users})
    def post(self, request, format=None):
        user = request.POST['user_username']
        return Response(UserSerializer(User.objects.filter(username__icontains=user), many=True).data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, SessionAuthentication])
def Add_img(request):
    img = request.FILES('img')
    user = request.user
    AdImage.objects.create(user_id=user.id, photo=img)
    return Response("Done")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, SessionAuthentication])
def Add_ads(request):
    user = request.user
    region = request.POST['region']
    category = request.POST['category']
    photo = request.POST.getlist['photo']
    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['price']
    Ads.objects.create(owner_id=user.id, region=region, category=category, photo=photo, name=name, date=datetime.datetime.now(), description=description, price=price)
    return Response("Done")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, SessionAuthentication])
def Users_ads(request):
    user = request.user
    return Response(AdsSerializer(Ads.objects.filter(owner_id=user.id), many=True).data)