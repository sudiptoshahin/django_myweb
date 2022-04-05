from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from django.contrib.auth.models import User
from news.models import News

# Create your views here.


def home(request):

    site = Main.objects.get(pk=1)
    newses = News.objects.all()

    return render(request, 'front/home.html', {'site': site, 'newses': newses})


def about(request):

    site = Main.objects.get(pk=1)

    return render(request, 'front/about.html', {'site': site})


def panel(request):

    return render(request, 'back/home.html')
