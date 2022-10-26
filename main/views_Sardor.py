from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required


def information(request):
    info = Information.objects.last()
    return render(request, 'information.html', {'info': info})



@login_required(login_url="sign_in")
def Add_reklama(request):
    user = request.user
    if user.status == 1:
        logo = request.FILES['img']
        company_name = request.POST['company_name']
        description = request.POST['description']
        Information.objects.create(company_name=company_name, logo=logo, description=description)
        return redirect('reklama')
    return redirect('sign-in')
