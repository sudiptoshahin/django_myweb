from django.shortcuts import render, get_object_or_404, redirect
from django.test import tag
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcat.models import SubCat
from cat.models import Cat
from trending.models import Trending
from django.contrib.auth.models import Group, User, Permission
import random
from comment.models import Comment

# Create your views here.

def news_detail(request, word):

    site = Main.objects.get(pk=1)
    newses = News.objects.all().order_by('-pk')
    cats = Cat.objects.all()
    subcats = SubCat.objects.all()

    shownews = News.objects.get(name=word)
    # popular newses
    popnewses = News.objects.order_by('-show')
    # tags 
    tagname = News.objects.get(name=word).tag
    tags = tagname.split(',')

    trendings = Trending.objects.order_by('-pk')

    try:
        mynews = News.objects.get(name=word)
        mynews.show = mynews.show + 1
        mynews.save()
    
    except:
        print('Can\'t add the show')

    code = News.objects.get(name=word).pk
    news_comments = Comment.objects.filter(news_id=code, status=1).order_by('-pk')
    count_cm = len(news_comments)

    return render(request, 'front/news_detail.html', {'site': site, 'newses': newses, 'cats': cats, 'subcats': subcats, 'shownews': shownews, 'popnewses': popnewses, 'tags': tags, 'trendings': trendings, 'code': code, 'news_comments': news_comments, 'count_cm': count_cm})

def news_detail_short(request, pk):

    site = Main.objects.get(pk=1)
    newses = News.objects.all().order_by('-pk')
    cats = Cat.objects.all()
    subcats = SubCat.objects.all()

    shownews = News.objects.get(rand=pk)
    # popular newses
    popnewses = News.objects.order_by('-show')
    # tags 
    tagname = News.objects.get(rand=pk).tag
    tags = tagname.split(',')

    trendings = Trending.objects.order_by('-pk')

    try:
        mynews = News.objects.get(rand=pk)
        mynews.show = mynews.show + 1
        mynews.save()
    
    except:
        print('Can\'t add the show')

    return render(request, 'front/news_detail.html', {'site': site, 'newses': newses, 'cats': cats, 'subcats': subcats, 'shownews': shownews, 'popnewses': popnewses, 'tags': tags, 'trendings': trendings})


def news_list(request):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    perms = Permission.objects.filter(user=request.user)
    for i in perms:
        if i.codename == 'master_user': perm = 1

    if perm == 0:
        newslist = News.objects.filter(writer=request.user)
    elif perm == 1:
        newslist = News.objects.all()

    return render(request, 'back/news_list.html', {'newslist': newslist, 'perm': perm})


def news_add(request):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

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

    date = str(year)+str(month)+str(day)
    randint = str(random.randint(1000, 9999))
    rand = date+randint
    rand = int(rand)
    print(rand)

    while len(News.objects.filter(rand=rand)) != 0:
        randint = str(random.randint(1000, 9999))
        rand = date+randint
        rand = int(rand)

    cats = SubCat.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newscatid = request.POST.get('newscat')
        tags = request.POST.get('tag')

        # forms validation
        if newstitle == '' or newstxtshort == '' or newstxt == '' or newscat == '':
            error = 'All fields required!'
            return render(request, 'back/error.html', {'error': error})

        try:
            # save the file
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            # print("----- "+str(myfile.content_type)+" ------")

            if str(myfile.content_type).startswith('image'):
                if myfile.size < 500000:

                    newscatname = SubCat.objects.get(pk=newscatid).name

                    ocatid = SubCat.objects.get(pk=newscatid).catid
                    ## add data to the database
                    data = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt,
                                date=today, time=time, picname=filename, picurl=url, writer=request.user,
                                catname=newscatname, catid=newscatid, ocatid=ocatid, show=0, tag=tags,
                                rand=rand)
                    data.save()

                    # get the subcat. origin id/pk
                    count = len(News.objects.filter(ocatid=ocatid))

                    b = Cat.objects.get(pk=ocatid)
                    b.count = count
                    b.save()

                    return redirect('news_list')
                else:

                    fs = FileSystemStorage()
                    fs.delete(filename)
                    
                    error = 'You uploaded file size is bigger than 5MB'
                    return render(request, 'back/error.html', {'error': error})
            else:

                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your uploaded file is not supported!"
                return render(request, 'back/error.html', {'error': error})
            
        except:
            error = 'Please input your news picture!'
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/news_add.html', {'cats': cats})


def news_del(request, pk):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    # get the news
    ''' We can also use the get() method insted of filter() but get() method 
    will shows error if it get a pk which is not exists. '''
    ''' We need also delete the image of the news so we need
    to use get() instead of filter() '''

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1
    
    if perm == 0:
        writer = News.objects.get(pk=pk).writer
        if str(writer) != str(request.user):
            error = 'Access Denied!'
            return render(request, 'back/error.html', {'error': error})
    
    try:
        news = News.objects.get(pk=pk)

        # delete the news image associated with it
        fs = FileSystemStorage()
        fs.delete(news.picname)

        ocatid = News.objects.get(pk=pk).ocatid

        news.delete()

        count = len(News.objects.filter(ocatid=ocatid))
        b = Cat.objects.get(pk=ocatid)
        b.count = count
        b.save()

    except:
        error = "Something is error."
        return render(request, 'back/error.html', {'error': error})


    return redirect('news_list')


def news_edit(request, pk):

    #login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    # study the page not found error
    if len(News.objects.filter(pk=pk)) == 0:
        error = 'News not found!'
        return redirect(request, 'back/error.html', {'error': error})

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        a = News.objects.get(pk=pk).writer
        if str(a) != str(request.user):
            error = 'Access Denied'
            return render(request, 'back/error.html', {'error': error})

    news = News.objects.get(pk=pk)
    cats = SubCat.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newscatid = request.POST.get('newscat')
        tags = request.POST.get('tag')

        try:
            # save the file
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith('image'):
                if myfile.size < 500000:

                    newscatname = SubCat.objects.get(pk=newscatid).name
                    ## add data to the database
                    
                    b = News.objects.get(pk=pk)

                    fss = FileSystemStorage()
                    fss.delete(b.picname)

                    b.name = newstitle
                    b.short_txt = newstxtshort
                    b.body_txt = newstxt
                    b.picname = filename
                    b.picurl = url
                    b.catname = newscatname
                    b.catid = newscatid
                    b.tag = tags
                    b.act = 0

                    b.save()

                    return redirect('news_list')
                else:

                    fs = FileSystemStorage()
                    fs.delete(filename)
                    
                    error = 'You uploaded file size is bigger than 5MB'
                    return render(request, 'back/error.html', {'error': error})
            else:

                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your uploaded file is not supported!"
                return render(request, 'back/error.html', {'error': error})
            
        except:
            newscatname = SubCat.objects.get(pk=newscatid).name
            ## add data to the database
                    
            b = News.objects.get(pk=pk)

            b.name = newstitle
            b.short_txt = newstxtshort
            b.body_txt = newstxt
            b.catname = newscatname
            b.catid = newscatid
            b.tag = tags

            b.save()

            return redirect('news_list')

    return render(request, 'back/news_edit.html', {'pk': pk, 'news': news, 'cats': cats})


def news_publish(request, pk):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    news = News.objects.get(pk=pk)
    news.act = 1
    news.save()


    return redirect('news_list')
