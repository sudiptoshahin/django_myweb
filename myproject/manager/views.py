from django.shortcuts import render, get_object_or_404, redirect
from .models import Manager
from django.contrib.auth.models import User
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from random import randint
# authenticating
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.

def manager_list(request):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    managers = Manager.objects.all().exclude(utxt='admin')

    return render(request, 'back/manager_list.html', {'managers': managers})


def manager_del(request, pk):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    manager = Manager.objects.get(pk=pk)
    b = User.objects.get(username=manager.utxt)
    b.delete()

    manager.delete()

    return redirect('manager_list')


def manager_group(request):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})

    groups = Group.objects.all().exclude(name='masteruser')

    return render(request, 'back/manager_group.html', {'groups': groups})


def manager_group_add(request):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST':
        name = request.POST.get('name')

        if name != '':
            if len(Group.objects.filter(name=name)) == 0:
                group = Group(name=name)
                group.save()
            else:
                error = 'This group name already been taken!'
                return render(request, 'back/error.html', {'error': error})

    return redirect('manager_group')


def manager_group_del(request, name):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})    

    b = Group.objects.filter(name=name)
    b.delete()

    return redirect('manager_group')


def users_groups(request, pk):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})

    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)

    user_groups = []
    for grp in user.groups.all():
        user_groups.append(grp.name)

    groups = Group.objects.all()

    return render(request, 'back/users_groups.html', {'user_groups': user_groups, 'groups': groups, 'pk': pk})


def add_users_to_groups(request, pk):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    if request.method == 'POST':
        gname = request.POST.get('gname')

        group = Group.objects.get(name=gname)
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.utxt)

        user.groups.add(group)

    return redirect('users_groups', pk=pk)

def del_users_from_groups(request, pk, name):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    group = Group.objects.get(name=name)
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)
    user.groups.remove(group)

    return redirect('users_groups', pk=pk)

def manager_permission(request):
    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})

    perms = Permission.objects.all()
    print(perms)

    return render(request, 'back/manager_permission.html', {'perms': perms})


def manager_permission_del(request, name):
    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})

    perms = Permission.objects.filter(name=name)
    perms.delete()

    return redirect('manager_permission')


def manager_permission_add(request):
    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST':
        name = request.POST.get('name')
        cname = request.POST.get('cname')

        if len(Permission.objects.filter(codename=cname)) == 0:
            content_type = ContentType.objects.get(app_label='main', model='main')
            permission = Permission.objects.create(codename=cname, name=name, content_type=content_type)
        else:
            error = 'Permission code name is used before!'
            return render(request, 'back/error.html', {'error': error})

    return redirect('manager_permission')


def users_permission(request, pk):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})

    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)

    permissions = Permission.objects.filter(user=user)

    # selected user permission
    user_permissions = []
    for perm in permissions:
        user_permissions.append(perm.name)

    # all permission
    permissions = Permission.objects.all()

    return render(request, 'back/user_permission.html', {'user_permissions': user_permissions, 'permissions': permissions, 'pk': pk})
 

def users_permission_add(request, pk):
    # login check
    if not request.user.is_authenticated:
         return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})
    

    if request.method == 'POST':
        pname = request.POST.get('pname')
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.utxt)

        perm = Permission.objects.get(name=pname)
        user.user_permissions.add(perm)

    return redirect('users_permission', pk=pk)
    


def users_permission_del(request, pk, name):

    # login check
    if not request.user.is_authenticated:
         return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})

    
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)

    permission = Permission.objects.get(name=name)
    user.user_permissions.remove(permission)

    return redirect('users_permission', pk=pk)


def groups_permissions(request, name):

    # login check
    if not request.user.is_authenticated:
         return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})

    group = Group.objects.get(name=name)
    permissions = group.permissions.all()

    all_permissions = Permission.objects.all()
    

    return render(request, 'back/groups_permissions.html', {'permissions': permissions, 'group_name': name, 'all_permissions': all_permissions})


def groups_permissions_del(request, gname, name):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})
    
    group = Group.objects.get(name=gname)
    perm = Permission.objects.get(name=name)
    group.permissions.remove(perm)
    
    return redirect('groups_permissions', name=gname)


def groups_permissions_add(request, name):

    # login check
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    perm = 0
    for group in request.user.groups.all():
        if group.name == 'masteruser': perm = 1

    if perm == 0:
        error = 'Access Denied!'
        return render(request, 'back/error.html', {'error': error})
    
    if request.method == 'POST':
        pname = request.POST.get('pname')

        group = Group.objects.get(name=name)
        perm = Permission.objects.get(name=pname)
        group.permissions.add(perm)
    
    return redirect('groups_permissions', name=name)


