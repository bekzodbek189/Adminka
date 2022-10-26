from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.contrib.auth.decorators import login_required



@login_required(login_url='sign-in')
def Sing_up(requset):
    if requset.method == 'POST':
        username = requset.POST['username']
        email = requset.POST['email']
        password = requset.POST['password']
        status = requset.POST.get('status')
        User.objects.create_user(username=username, email=email, password=password, status=status)
        return redirect('sign-in')
    return render(requset, 'pages-sign-up.html')



def Sing_in(request):
    user = request.user
    if user.status == 1:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            users = User.objects.filter(username=username)
            if users is not None:
                usr = authenticate(username=username, password=password)
                if usr is not None:
                    login(request, usr)
                    return redirect('dashboart')
                else:
                    return redirect('sign-up')
            else:
                return redirect('sign-up')
    return render(request, 'pages-sign-in.html')
    

@login_required(login_url='sign-in')
def Logout(request):
    logout(request)
    return redirect('sign-in')


@login_required(login_url='sign-in')
def Dashboart(request):
    user = request.user
    if user.status == 1:
        return render(request, 'dashboard.html')
    return redirect("sign-in")

@login_required(login_url='sign-in')
def UpdateUser(request):
    user = request.user
    if user.status == 1:
        if request.method == "POST":
            username = request.POST['username']
            current = request.POST['current']
            password = request.POST['password']
            usr = authenticate(username=user.username, password=current)
            if usr is not None:
                print('z')
                user.username = username
                user.set_password(password)
                user.save()
                return redirect('sign-in')
            else:
                return redirect('dashboart')
        else:
            return render(request, "pages-update.html")
    return redirect('sign-in')

@login_required(login_url='sign-in')
def Profile(request):
    user = request.user
    con = {
        "ads": Ads.objects.filter(owner=user)
    }
    return render(request, 'pages-profile.html', con)






