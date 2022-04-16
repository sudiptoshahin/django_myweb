from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcat.models import SubCat
from cat.models import Cat

# Create your views here.

def news_detail(request, word):

    site = Main.objects.get(pk=1)
    news = News.objects.filter(name=word).first()

    return render(request, 'front/news_detail.html', {'news': news, 'site': site})


def news_list(request):

    newslist = News.objects.all()

    return render(request, 'back/news_list.html', {'newslist': newslist})


def news_add(request):

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

    cats = SubCat.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newscatid = request.POST.get('newscat')

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
                                date=today, time=time, picname=filename, picurl=url, writer='-',
                                catname=newscatname, catid=newscatid, ocatid=ocatid, show=0)
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

    # get the news
    ''' We can also use the get() method insted of filter() but get() method 
    will shows error if it get a pk which is not exists. '''
    ''' We need also delete the image of the news so we need
    to use get() instead of filter() '''
    
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

    # study the page not found error
    if len(News.objects.filter(pk=pk)) == 0:
        error = 'News not found!'
        return redirect(request, 'back/error.html', {'error': error})

    news = News.objects.get(pk=pk)
    cats = SubCat.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newscatid = request.POST.get('newscat')

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

            b.save()

            return redirect('news_list')

    return render(request, 'back/news_edit.html', {'pk': pk, 'news': news, 'cats': cats})