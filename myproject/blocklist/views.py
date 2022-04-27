from django.shortcuts import render, get_object_or_404, redirect
from .models import BlockList
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.core.files.storage import FileSystemStorage
from trending.models import Trending

# Create your views here.

def block_list(request):

    blocklists = BlockList.objects.all()

    return render(request, 'back/block_list.html', {'blocklists': blocklists})


def add_blocked_ip(request):

    if request.method == 'POST':
        ip_addr = request.POST.get('ip_addr')

        if ip_addr != '':
            b = BlockList(ip=ip_addr)
            b.save()

    return redirect('block_list')


def del_blocked_ip(request, pk):

    blocked_ip = BlockList.objects.filter(pk=pk)
    blocked_ip.delete()

    return redirect('block_list')