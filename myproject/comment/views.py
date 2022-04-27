from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from manager.models import Manager
import datetime

# Create your views here.


def news_cm_add(request, pk):

    if request.method == 'POST':
        
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day

        hour = now.hour
        minute = now.minute

        if len(str(day)) == 1:
            day = '0' + str(day)
        if len(str(month)) == 1:
            month = '0' + str(month)
        
        today = str(year) + '/' + str(month) + '/' + str(day)
        time = str(hour) + ':' + str(minute)

        cm_msg = request.POST.get('comment_txt')

        if request.user.is_authenticated:
            manager = Manager.objects.get(utxt=request.user)

            b = Comment(name=manager.name, email=manager.email, cm=cm_msg, news_id=pk, date=today, time=time)
            b.save()
        else:
            user_name = request.POST.get('name')
            user_email = request.POST.get('email')

            d = Comment(name=user_name, email=user_email, cm=cm_msg, news_id=pk, date=today, time=time)
            d.save()


    newsname = News.objects.get(pk=pk).name

    return redirect('news_detail', word=newsname)


def news_cm_list(request):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error': error})

    comments = Comment.objects.all()

    return render(request, 'back/news_comments.html', {'comments': comments}) 


def news_cm_del(request, pk):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error': error})

    comment = Comment.objects.filter(pk=pk)
    comment.delete()

    return redirect('news_comments')


def news_cm_confirmed(request, pk):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error': error})

    comment = Comment.objects.get(pk=pk)
    comment.status = 1
    comment.save()

    return redirect('news_comments')

