from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from .models import Main
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from random import randint
# authenticating
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from manager.models import Manager

# Create your views here.


def home(request):

    site = Main.objects.get(pk=1)
    newses = News.objects.all().order_by('-pk')
    cats = Cat.objects.all()
    subcats = SubCat.objects.all()
    # latest or last news
    lastnewses = News.objects.order_by('-pk')[:3]

    # popular news
    popnewses = News.objects.order_by('-show')
    popnewses2 = News.objects.order_by('-show')[:3]

    trendings = Trending.objects.order_by('-pk')[:5]

    random_obj = Trending.objects.all()[randint(0, len(trendings) - 1)]

    return render(request,
                 'front/home.html',
                  {'site': site, 'newses': newses, 'cats': cats,
                    'subcats': subcats, 'lastnewses': lastnewses,
                    'popnewses': popnewses, 'popnewses2': popnewses2, 
                    'trendings': trendings})


def about(request):

    site = Main.objects.get(pk=1)
    newses = News.objects.all().order_by('-pk')
    cats = Cat.objects.all()
    subcats = SubCat.objects.all()
    # latest or last news
    lastnewses = News.objects.order_by('-pk')[:3]

    # popular news
    popnewses = News.objects.order_by('-show')
    popnewses2 = News.objects.order_by('-show')[:3]

    trendings = Trending.objects.order_by('-pk')[:5]

    return render(request, 'front/about.html', {'site': site, 'newses': newses, 'cats': cats, 'subcats': subcats, 'lastnewses': lastnewses, 'popnewses': popnewses, 'popnewses2': popnewses2, 'trendings': trendings})


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


def about_setting(request):

    # check login
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    if request.method == 'POST':
        txt = request.POST.get('abouttxt')

        if txt == '':
            error = 'Please fill the about section!'
            return render(request, 'back/error.html', {'error': error})

        main = Main.objects.get(pk=1)
        main.abouttxt = txt
        main.save()

    abouttxt = Main.objects.get(pk=1).abouttxt

    return render(request, 'back/about_setting.html', {'abouttxt': abouttxt})


def contact(request):
    site = Main.objects.get(pk=1)
    newses = News.objects.all().order_by('-pk')
    cats = Cat.objects.all()
    subcats = SubCat.objects.all()
    # latest or last news
    lastnewses = News.objects.order_by('-pk')[:3]

    # popular news
    popnewses = News.objects.order_by('-show')
    popnewses2 = News.objects.order_by('-show')[:3]

    trendings = Trending.objects.order_by('-pk')[:5]

    return render(request, 'front/contact.html', {'site': site, 'newses': newses, 'cats': cats, 'subcats': subcats, 'lastnewses': lastnewses, 'popnewses': popnewses, 'popnewses2': popnewses2, 'trendings': trendings})


def change_pass(request):

    # login check
    if not request.user.is_authenticated:
        redirect('login')
    # login check end

    if request.method == 'POST':
        old_pass = request.POST.get('oldpass')
        new_pass = request.POST.get('newpass')
        
        if old_pass == '' or new_pass == '':
            error = 'All fields are required!'
            return render(request, 'back/error.html', {'error': error})

        user = authenticate(username=request.user, password=old_pass)

        if user != None:
            if len(new_pass) < 5:
                error = 'You password atleast 5 character!'
                return render(request, 'back/error.html', {'error': error})

            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            for i in new_pass:
                if i > '0' and i < '9':
                    count1 = 1
                if i > 'a' and i < 'z':
                    count2 = 1
                if i > 'A' and i < 'Z':
                    count3 = 1
                if i > '!' and i < '(':
                    count4 = 1
            
            if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1:
                user = User.objects.get(username=request.user)
                user.set_password(new_pass)
                user.save()
                return redirect('logout')

        else:
            error = 'Your password is not correct'
            return render(request, 'back/error.html', {'error': error})


    return render(request, 'back/changepass.html')


def my_register(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if name == '':
            msg = 'Please input your name'
            return render(request, 'front/msgbox.html')

        # password validations
        if password1 != password2:
            msg = 'Password didn\'t match!'
            return render(request, 'front/msgbox.html', {'msg': msg})

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for ch in password1:
            if ch > '0' and ch < '9':
                count1 = 1
            if ch > 'A' and ch < 'Z':
                count2 = 1
            if ch > 'a' and ch < 'z':
                count3 = 1
            if ch > '!' and ch < '(':
                count4 = 1
        if count1 == 0 or count2 == 0 or count3 == 0 or count4 == 0:
            msg = "Your password is not strong enough!"
            return render(request, 'front/msgbox.html', {'msg': msg})
        if len(password1) < 5:
            msg = 'Your password must be 5 character long!'
            return render(request, 'front/msgbox.html', {'msg': msg})

        # username validations/ userrname & email exists or not
        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0:
            user = User.objects.create_user(username=uname, email=email, password=password1)
            b = Manager(name=name, utxt=uname, email=email)
            b.save()


    return render(request, 'front/login.html')