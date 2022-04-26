from tabnanny import check
from django.shortcuts import render, get_object_or_404, redirect
from .models import Newsletter
from django.contrib.auth.models import User
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
import re

# Create your views here.

def news_letter(request):

    if request.method == 'POST':
        txt = request.POST.get('txt')
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, txt):
            newsletter = Newsletter(txt=txt, status=1)
            newsletter.save()
        else:
            try:
                txt = int(txt)
                newsletter = Newsletter(txt=txt, status=2)
                newsletter.save()
            except:
                return redirect('home')

    return redirect('home')


def news_letter_emails(request):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    emails = Newsletter.objects.filter(status=1)

    return render(request, 'back/newsletter_emails.html', {'emails': emails})


def news_letter_phones(request):
    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    phones = Newsletter.objects.filter(status=2)

    return render(request, 'back/newsletter_phonenumber.html', {'phones': phones})


def news_letter_txt_del(request, pk, status):
    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    newsletter = Newsletter.objects.get(pk=pk)
    newsletter.delete()

    if int(status) == 2:
        return redirect('news_letter_phones')

    return redirect('news_letter_emails')


