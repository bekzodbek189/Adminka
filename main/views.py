from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.contrib.auth.decorators import login_required



def Sing_in(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        users = User.objects.filter(username=username)
        if users is not None:
            usr = authenticate(username=username, password=password)
            if usr is not None:
                if usr.status == 1:
                    login(request, usr)
                    return redirect('dashboard')
                return redirect('sign_up')
            else:
                return redirect('sign_up')
        else:
            return redirect('sign_up')
    return render(request, "pages-sign-in.html")

@login_required(login_url='sign_in')
def Logout(request):
    logout(request)
    return redirect('sign_in')


@login_required(login_url='sign_in')
def Dashboart(request):
    user = request.user
    if user.status == 1:
        return render(request, 'dashboard.html', {"user": user})
    return redirect("sign_in")

@login_required(login_url='sign_in')
def UpdateUser(request):
    user = request.user
    if user.status == 1:
        if request.method == "POST":
            username = request.POST['username']
            current = request.POST['current']
            password = request.POST['password']
            usr = authenticate(username=user.username, password=current)
            if usr is not None:
                user.username = username
                user.set_password(password)
                user.save()
                return redirect('sign_in')
            else:
                return redirect('dashboart')
        else:
            return render(request, "pages-update.html")
    return redirect('sign_in')



@login_required(login_url='sign_in')
def Profile(request):
    user = request.user
    con = {
        "ads": Ads.objects.filter(owner=user)
    }
    return render(request, 'pages-profile.html', con)


@login_required(login_url='sign-in')
def Subcategory_add(request):
    con = {
        'category': Category.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        Subcategory.objects.create(name=name, category_id=category)
        return redirect('subcategorys')
    return render(request, 'sub_add.html.html', con)


@login_required(login_url='sign-in')
def Subcategoys(request):
    con = {
        "subcategorys": Subcategory.objects.filter(status=1).order_by('-id')
    }
    return render(request, 'subcategories.html', con)

@login_required(login_url='sign-in')
def Subcategory_change(request, pk):
    sub = Subcategory.objects.get(id=pk)
    con = {
        'pk': pk,
        'category': Category.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        sub.name = name
        sub.category.id = category
        sub.save()
        return redirect('subcategorys')
    return render(request, 'sub_cange.html', con)

@login_required(login_url='sign-in')
def Sub_delete(request, pk):
    user = request.user
    sub = Subcategory.objects.get(id=pk)
    if sub.status == 1:
        sub.status = 2
        sub.save()
    return redirect('subcategorys')



@login_required(login_url='sign-in')
def Regions(request):
    con = {
        "region": Region.objects.filter(status=1).order_by('-id')
    }
    return render(request, 'regions.html', con)


@login_required(login_url='sign-in')
def Region_add(request):
    con = {
        'district': District.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        district = request.POST['district']
        Region.objects.create(name=name, district_id=district)
        return redirect('regions')
    return render(request, 'region_add.html', con)


@login_required(login_url='sign-in')
def Region_change(request, pk):
    region = Region.objects.get(id=pk)
    con = {
        'pk': pk,
        'district': District.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        district = request.POST['district']
        region.name = name
        region.district.id = district
        region.save()
        return redirect('regions')
    return render(request, 'region_change.html', con)


@login_required(login_url='sign-in')
def Region_delete(request, pk):
    region = Region.objects.get(id=pk)
    if region.status == 1:
        region.status = 2
        region.save()
    return redirect('regions')



@login_required(login_url='sign-in')
def Districts(request):
    con = {
        "district": District.objects.filter(status=1).order_by('-id')
    }
    return render(request, 'districts.html', con)


@login_required(login_url='sign-in')
def Distrtict_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        District.objects.create(name=name)
        return redirect('districts')
    return render(request, 'district_add.html')


@login_required(login_url='sign-in')
def District_change(request, pk):
    district = District.objects.get(id=pk)
    con = {
        'pk': pk,
    }
    if request.method == 'POST':
        name = request.POST['name']
        district.name = name
        district.save()
        return redirect('districts')
    return render(request, 'district_change.html', con)


@login_required(login_url='sign-in')
def District_delete(request, pk):
    district = District.objects.get(id=pk)
    if district.status == 1:
        district.status = 2
        district.save()
    return redirect('districts')

