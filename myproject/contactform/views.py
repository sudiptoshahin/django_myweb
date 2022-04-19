from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactForm
from main.models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.core.files.storage import FileSystemStorage
import datetime

def contact_add(request):

    site = Main.objects.get(pk=1)
    newses = News.objects.all().order_by('-pk')
    cats = Cat.objects.all()
    subcats = SubCat.objects.all()
    # latest or last news
    lastnewses = News.objects.order_by('-pk')[:3]

    # popular news
    popnewses = News.objects.order_by('-show')
    popnewses2 = News.objects.order_by('-show')[:3]

    #----------------date and time -----------
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
    #--------------- date and time ------------

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        txt = request.POST.get('msg')

        if name == '' or email == '' or txt == '':
            msg = 'All fields are required!'
            return render(request, 'front/msgbox.html', {'msg': msg, 'site': site, 'newses': newses, 'cats': cats, 'subcats': subcats, 'lastnewses': lastnewses, 'popnewses': popnewses, 'popnewses2': popnewses2})

        b = ContactForm(name=name, email=email, txt=txt, date=today, time=time)
        b.save()

        msg = "Your message is received!"
        return render(request, 'front/msgbox.html', {'msg': msg, 'site': site, 'newses': newses, 'cats': cats, 'subcats': subcats, 'lastnewses': lastnewses, 'popnewses': popnewses, 'popnewses2': popnewses2})

    return render(request, 'front/msgbox.html', {'msg': msg, 'site': site, 'newses': newses, 'cats': cats, 'subcats': subcats, 'lastnewses': lastnewses, 'popnewses': popnewses, 'popnewses2': popnewses2})


def contact_show(request):

    # check login
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    contacts = ContactForm.objects.all()

    return render(request, 'back/contact_form.html', {'contacts': contacts})


def contact_del(request, pk):
    # check login
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end
    contact = ContactForm.objects.filter(pk=pk)
    contact.delete()

    return redirect('contact_show')

    