from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat

# Create your views here.

def cat_list(request):

    cats = Cat.objects.all()

    return render(request, 'back/cat_list.html', {'cats': cats})


def cat_add(request):

    if request.method == 'POST':
        name = request.POST.get('name')

        if name == '':
            error = 'All fields are required.'
            return render(request, 'back/error.html', {'error': error})

        if len(Cat.objects.filter(name=name)) != 0:
            error = 'This category name is taken already.'
            return render(request, 'back/error.html', {'error': error})
        
        cat = Cat(name=name)
        cat.save()
        return redirect('cat_list')

    return render(request, 'back/cat_add.html')