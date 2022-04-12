from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCat
from cat.models import Cat

# Create your views here.

def subcat_list(request):

    subcats = SubCat.objects.all()

    return render(request, 'back/subcat_list.html', {'subcats': subcats})


def subcat_add(request):

    cats = Cat.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        catid = request.POST.get('cat')

        if name == '':
            error = 'All fields are required!'
            return render(request, 'back/error.html', {'error': error})

        if len(SubCat.objects.filter(name=name)) != 0:
            error = 'The name already taken!'
            return render(request, 'back/error.html', {'error': error})

        catname = Cat.objects.get(pk=catid)

        subcat = SubCat(name=name, catname=catname.name, catid=catid)
        subcat.save()
        return redirect('subcat_list')

    return render(request, 'back/subcat_add.html', {'cats': cats})