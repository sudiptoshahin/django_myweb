from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime

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

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')

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
                    ## add data to the database
                    data = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today, time=time, picname=filename, picurl=url, writer='-', catname=newscat, catid=0, show=0)
                    data.save()
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

    return render(request, 'back/news_add.html')


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

        news.delete()
    except:
        error = "Something is error."
        return render(request, 'back/error.html', {'error': error})


    return redirect('news_list')