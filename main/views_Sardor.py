from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required


def information(request):
    info = Information.objects.order_by('-id')
    return render(request, 'information.html', {'info': info})



@login_required(login_url="sign_in")
def Add_info(request):
    user = request.user
    if user.status == 1:
        logo = request.FILES['logo']
        company_name = request.POST['company_name']
        description = request.POST['description']
        Information.objects.create(company_name=company_name, logo=logo, description=description)
        return redirect('information')
    return redirect('sign-in')




def change_info(request, pk):
    user = request.user
    info = Information.objects.get(id=pk)

    if user.status == 1:
        logo = request.FILES['logo']
        company_name = request.POST['company_name']
        description = request.POST['description']
        info.logo = logo
        info.company_name = company_name
        info.description = description
        info.save()
        return redirect("information")
    return render(request, 'change_information.html')


@login_required(login_url="sign_in")
def delete_info(request, pk):
    user = request.user
    if user.status == 1:
        info = Information.objects.get(id=pk)
        info.status = 2
        info.save()
        return redirect('information')
    return redirect('sign-in')