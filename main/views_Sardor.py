from django.shortcuts import redirect, render
from .models import *


def information(request):
    return render(request, 'information.html')
