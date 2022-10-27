from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required


def information(request):
    info = Information.objects.order_by('-id')
    return render(request, 'information.html', {'info': info})



@login_required(login_url="sign_in")
def Add_info(request):
    user = request.user
    if request.method == "POST":
        if user.status == 1:
            logo = request.FILES['logo']
            company_name = request.POST['company_name']
            description = request.POST['description']
            Information.objects.create(company_name=company_name, logo=logo, description=description)
            return redirect('information')
    return render(request, 'ad_information.html'
                  )




def change_info(request, pk):
    user = request.user
    info = Information.objects.get(id=pk)
    if request.method == "POST":
        if user.status == 1:
            logo = request.FILES['logo']
            company_name = request.POST['company_name']
            description = request.POST['description']
            info.logo = logo
            info.company_name = company_name
            info.description = description
            info.save()
            return redirect("information")
    return render(request, 'change_information.html', {'info': info})


@login_required(login_url="sign_in")
def delete_info(request, pk):
    user = request.user
    if user.status == 1:
        info = Information.objects.get(id=pk)
        info.delete()
        return redirect('information')
    return redirect('sign-in')





def region(request):
    reg = Region.objects.all()
    return render(request, 'region.html', {'reg': reg})



@login_required(login_url="sign_in")
def add_reg(request):
    user = request.user
    if request.method == "POST":
        if user.status == 1:
            name = request.POST['name']
            Region.objects.create(name=name)
    return redirect('region')
    return render(request, 'add_region.html')




def change_reg(request, pk):
    user = request.user
    reg = Region.objects.get(id=pk)
    if request.method == "POST":
        if user.status == 1:
            name = request.POST['name']
            reg.name = name
            reg.save()
            return redirect("region")
    return render(request, 'change_region.html', {'reg': reg})


@login_required(login_url="sign_in")
def delete_reg(request, pk):
    user = request.user
    if user.status == 1:
        reg = Region.objects.get(id=pk)
        reg.delete()
        return redirect('region')
    return redirect('sign-in')