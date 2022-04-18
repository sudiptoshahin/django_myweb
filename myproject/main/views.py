from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from django.contrib.auth.models import User
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from .models import Main
from django.core.files.storage import FileSystemStorage

# authenticating
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):

    site = Main.objects.get(pk=1)
    newses = News.objects.all().order_by('-pk')
    cats = Cat.objects.all()
    subcats = SubCat.objects.all()
    # latest or last news
    lastnewses = News.objects.order_by('-pk')[:3]

    return render(request, 'front/home.html', {'site': site, 'newses': newses, 'cats': cats, 'subcats': subcats, 'lastnewses': lastnewses})


def about(request):

    site = Main.objects.get(pk=1)

    return render(request, 'front/about.html', {'site': site})


def panel(request):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    return render(request, 'back/home.html')


def my_login(request):

    if request.method == 'POST':
        unametxt = request.POST.get('username')
        upasstxt = request.POST.get('password')

        if unametxt != '' and upasstxt != '':
            user = authenticate(username=unametxt, password=upasstxt)

            if user != None:
                login(request, user)
                return redirect('panel')

    return render(request, 'front/login.html')


def my_logout(request):

    logout(request)

    return redirect('login')


def site_setting(request):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    if request.method == 'POST':
        name = request.POST.get('sitetitle')
        about = request.POST.get('abouttxt')
        tel = request.POST.get('sitetel')
        fb = request.POST.get('fblink')
        tw = request.POST.get('twlink')
        yt = request.POST.get('ytlink')
        link = request.POST.get('link')

        if fb == '': fb = '#'
        if tw == '': tw = '#'
        if yt == '': yt = '#'
        if link == '': link = '#'

        if name == '' or tel == '' or about == '':
            error = 'All fields are required!'
            return render(request, 'back/error.html', {'error': error})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            picname = filename
            picurl = url
        except:
            picname = '-'
            picurl = '-'

        try:
            myfile2 = request.FILES['myfile2']
            fs = FileSystemStorage()
            filename2 = fs.save(myfile2.name, myfile2)
            url2 = fs.url(filename2)

            picname2 = filename2
            picurl2 = url2
        except:
            picname2 = '-'
            picurl2 = '-'
        
        b = Main.objects.get(pk=1)
        b.name = name
        b.about = about
        b.tel = tel
        b.fb = fb
        b.tw = tw
        b.yt = yt
        b.link = link
        if picname != '-': b.picname = picname
        if picurl != '-': b.picurl = picurl
        
        if picname2 != '-': b.picname2 = picname2
        if picurl2 != '-': b.picurl2 = picurl2
        
        b.save()

    site = Main.objects.get(pk=1)

    return render(request, 'back/settings.html', {'site': site})
