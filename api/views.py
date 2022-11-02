from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from .serializers import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from ipware import get_client_ip

@api_view(['POST'])
def sold_ads(request, pk):
    status = Ads.objects.get(id=pk)
    if status.status == 1:
        status.status = 4
        status.save()
        return Response('ok')


@api_view(['POST'])
def Register_user(request):
    phone = request.POST['name']
    password = request.POST['password']
    if phone.startswith('+998'):
        phones = phone[1:13]
        if phones.isnumeric():
            if len(phones) == 12:
                User.objects.create_user(username=phones, password=password)
                return Response('ok')
            else:
                return Response('net')
        else:
            return Response('yoq')
    else:
        return Response('zor')


@api_view(['POST'])
def Login_user(request):
    phone = request.POST['phone']
    password = request.POST['password']
    users = User.objects.filter(username=phone)
    if users is not None:
        usr = authenticate(username=phone, password=password)
        if usr is not None:
            login(request, usr)
            return Response('ok')
        return Response('no')
    return Response('salom')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, SessionAuthentication])
def Change_user(request):
    user = request.user
    password = request.POST['password']
    username = request.POST['username']
    current = request.POST['current']
    usr = authenticate(username=user.username, password=current)
    if usr is not None:
        user.username = username
        user.set_password(password)
        user.save()
        return Response('ok')
    else:
        return Response('no')




@api_view(['POST'])
def wishlistadd(request, ):
    ads_id = request.POST['ads_id']
    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        return Response({"Unable to get the client's IP address"})
    else:
        Wishlist.objects.create(ip=client_ip, ads_id=ads_id)
        return Response({"added"})

class InformationView(ReadOnlyModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


class AboutView(ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer



class ReklamaView(ReadOnlyModelViewSet):
    queryset = Reklama.objects.all()
    serializer_class = ReklamaSerializer


