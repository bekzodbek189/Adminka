from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url="sign_in")
def Themes(request):
    user = request.user
    if user.status == 1:
        if request.method == "POST":
            text = request.POST.get("theme")
            Theme.objects.create(therme=text)
            return redirect("change")
        elif request.method == 'GET':
            text = request.GET.get("theme")
            a = Theme.objects.last()
            a.theme = text
            a.save()
            return redirect("change")
        else:
            return redirect("change")
    return redirect('pages-404.html')

@login_required(login_url="sign_in")
def Create_About(request):
    """ Create information about """
    user = request.user
    if user.status == 1:
        if request.method == "POST":
            text = request.POST.get("title")
            logo = request.FILES.get("logo")
            About.objects.create(txt=text, logo=logo)
            return redirect("page_about")
        return render(request, "add_about.html")
    return redirect('pages-404.html')

def Sing_up(requset):
    """ Register """
    if requset.method == 'POST':
        username = requset.POST['username']
        email = requset.POST['email']
        password = requset.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('sign_in')
    return render(requset, 'pages-sign-up.html')

@login_required(login_url="sign_in")
def Pages_blank(request):
    """ Go to page blank """
    user = request.user
    if user.status == 1:
        context = {
            "ads": Ads.objects.filter(status=1)
        }
        return render(request, "pages-blank.html", context)
    return redirect('pages-404.html')

def Pages_sing_in(request):
    """ Go to page Sign in """
    return render(request, "pages-sign-in.html")

@login_required(login_url="sign_in")
def Users(request):
    """ Go to page User """
    user = request.user
    if user.status == 1:
        context = {
            "users": User.objects.filter(status=2)
        }
        return render(request, "users.html", context)
    return redirect('pages-404.html')

@login_required(login_url="sign_in")
def Search(request):
    """ Search users """
    user = request.user
    if user.status == 1:
        name = request.GET['name']
        context = {
            "users": User.objects.filter(username__icontains=name, status=2)
        }
        return render(request, "users.html", context)
    return redirect('pages-404.html')

@login_required(login_url="sign_in")
def Accepted(request, pk):
    """ Change Product's status """
    user = request.user
    if user.status == 1:
        ads = Ads.objects.get(id=pk)
        ads.status = 2
        ads.save()
        return redirect('blank')
    return redirect('pages-404.html')

@login_required(login_url="sign_in")
def Rejected(request, pk):
    """ Change Product's status """
    user = request.user
    if user.status == 1:
        ads = Ads.objects.get(id=pk)
        ads.status = 3
        ads.save()
        return redirect('blank')
    return redirect('pages-404.html')

@login_required(login_url="sign_in")
def Page_accepted(request):
    """ Go to page which Product's status = accepted """
    user = request.user
    if user.status == 1:
        context = {
            "ads": Ads.objects.filter(status=2)
        }
        return render(request, "pages-blank.html", context)
    return redirect('pages-404.html')

@login_required(login_url="sign_in")
def Page_rejected(request):
    """ Go to page which Ads's status = rejected """
    user = request.user
    if user.status == 1:
        context = {
            "ads": Ads.objects.filter(status=3)
        }
        return render(request, "pages-blank.html", context)
    return redirect('pages-404.html')

@login_required(login_url="sign_in")
def Is_top(request, pk):
    """ Change Product's is_top field """
    user = request.user
    if user.status == 1:
        top = Ads.objects.get(id=pk)
        if top.is_top == True:
            top.is_top = False
        else:
            top.is_top = True
        top.save()
        return redirect('dashboard')
    return redirect('pages-404.html')

@login_required(login_url="sign_in")
def Is_recommended(request, pk):
    user = request.user
    if user.status == 1:
        recommended = Ads.objects.get(id=pk)
        if recommended.is_recommended == True:
            recommended.is_recommended = False
        else:
            recommended.is_recommended = True
        recommended.save()
        return redirect('dashboard')
    return redirect('pages-404.html')

@login_required(login_url="sign_in")
def Page_is_top(request):
    user = request.user
    if user.status == 1:
        return render(request, "pages-blank.html", {"ads": Ads.objects.filter(is_top=True)})
    return redirect('pages-404.html')

@login_required(login_url="sign_in")
def Page_is_recommended(request):
    user = request.user
    if user.status == 1:
        context = {
            "ads": Ads.objects.filter(is_recommended=True)
        }
        return render(request, "pages-blank.html", context)
    return redirect('sign_in')

@login_required(login_url="sign_in")
def Page_reklama(request):
    user = request.user
    if user.status == 1:
        context = {
            "reklama": Reklama.objects.filter(status=1)
        }
        return render(request, "reklama.html", context)
    return redirect('sign_in')

@login_required(login_url="sign_in")
def Change_Reklama(request, pk):
    user = request.user
    if user.status == 1:
        reklama = Reklama.objects.get(id=pk)
        img = request.FILES['img']
        title = request.POST['title']
        text = request.POST['text']
        link = request.POST['link']
        reklama.img = img
        reklama.title = title
        reklama.text = text
        reklama.link = link
        reklama.save()
        return redirect('reklama')
    return redirect('sign_in')

@login_required(login_url="sign_in")
def Delete_Reklama(request, pk):
    user = request.user
    if user.status == 1:
        reklama = Reklama.objects.get(id=pk)
        reklama.status = 2
        reklama.save()
        return redirect('reklama')
    return redirect('sign_in')

@login_required(login_url="sign_in")
def Page_Change_Reklama(request, pk):
    user = request.user
    if user.status == 1:
        return render(request, "change_reklama.html", {"pk": pk})
    return redirect('sign_in')

@login_required(login_url="sign_in")
def Page_Add_Reklama(request):
    user = request.user
    if user.status == 1:
        return render(request, "add_reklama.html")
    return redirect('sign_in')

@login_required(login_url="sign_in")
def Add_reklama(request):
    user = request.user
    if user.status == 1:
        img = request.FILES['img']
        title = request.POST['title']
        text = request.POST['text']
        link = request.POST['link']
        Reklama.objects.create(title=title, text=text, link=link, img=img)
        return redirect('reklama')
    return redirect('sign_in')

@login_required(login_url="sign_in")
def Page_about(request):
    user = request.user
    if user.status == 1:
        context = {
            "about": About.objects.last()
        }
        return render(request, 'about.html', context)
    return redirect('sign-in')

@login_required(login_url="sign_in")
def Page_information(request):
    user = request.user
    if user.status == 1:
        context = {
            "info": Information.objects.last()
        }
        return render(request, 'information.html', context)
    return redirect('pages-404.html')

def Delete_about(request, pk):
    a = About.objects.get(id=pk)
    a.status = 2
    a.save()
    return redirect('page_about')

def Page_category(request):
    return render(request, "category.html", {"category": Category.objects.filter(status=1)})

def Change_category(request, pk):
    if request.method == "POST":
        name = request.POST['name']
        img = request.FILES['img']
        a = Category.objects.get(id=pk)
        a.name = name
        a.photo = img
        a.save()
        return redirect('page_category')
    context = {
        "pk": pk
    }
    return render(request, "change_category.html", context)

def Create_category(request):
    if request.method == "POST":
        name = request.POST['name']
        img = request.FILES['img']
        Category.objects.create(name=name, photo=img)
        return redirect('page_category')
    return redirect('page_category')

def Delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.status = 2
    category.save()
    return redirect('page_category')

@login_required(login_url="sign_in")
def Create_information(request):
    """ Create information a lot """
    user = request.user
    if user.status == 1:
        if request.method == "POST":
            company_name = request.POST["company_name"]
            logo = request.FILES["logo"]
            description = request.POST["description"]
            googleplay = request.POST["googleplay"]
            appstore = request.POST["appstore"]
            Information.objects.create(company_name=company_name, logo=logo, description=description, googleplay=googleplay, appstore=appstore)
            return redirect('information')
        return render(request, "ad_information.html")
    return redirect('pages-404.html')

def Change_information(request, pk):
    if request.method == "POST":
        company_name = request.POST["company_name"]
        logo = request.FILES["logo"]
        description = request.POST["description"]
        googleplay = request.POST["googleplay"]
        appstore = request.POST["appstore"]
        info = Information.objects.get(id=pk)
        info.company_name = company_name
        info.logo = logo
        info.description = description
        info.googleplay = googleplay
        info.appstore = appstore
        info.save()
        return redirect('information')
    return render(request, "change_information.html", {"pk": pk})

def Delete_information(request, pk):
    info = Information.objects.get(id=pk)
    info.status = 2
    info.save()
    return redirect('information')

def Change_about(request, pk):
    if request.method == "POST":
        text = request.POST["text"]
        logo = request.FILES["logo"]
        about = About.objects.get(id=pk)
        about.txt = text
        about.logo = logo
        about.save()
        return redirect("page_about")
    return render(request, "change_about.html", {"pk": pk})