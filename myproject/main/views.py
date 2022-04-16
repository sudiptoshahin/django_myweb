from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from django.contrib.auth.models import User
from news.models import News
from cat.models import Cat
from subcat.models import SubCat

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

    return render(request, 'back/home.html')
