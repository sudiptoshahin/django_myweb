from django.shortcuts import render, get_object_or_404, redirect
from .models import Trending
from django.contrib.auth.models import User
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from main.models import Main
from django.core.files.storage import FileSystemStorage
# Create your views here.


def trending_add(request):

    if request.method == 'POST':
        txt = request.POST.get('txt')

        if txt == '':
            error = 'Field is required'
            return render(request, 'back/error.html', {'error': error})

        b = Trending(txt=txt)
        b.save()

    trendings = Trending.objects.all()[:5]



    return render(request, 'back/trending.html', {'trendings': trendings})


def trending_del(request, pk):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end
    b = Trending.objects.filter(pk=pk)
    b.delete()

    return redirect('trending_add')


def trending_edit(request, pk):
    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    if request.method == 'POST':
        txt = request.POST.get('txt')

        if txt == '':
            error = 'Fields must be required!'
            return render(request, 'back/error.html', {'error': error})

        b = Trending.objects.get(pk=pk)
        b.txt = txt
        b.save()
        return redirect('trending_add')
        

    trending = Trending.objects.get(pk=pk)

    return render(request, 'back/trending_edit.html', {'trending': trending})