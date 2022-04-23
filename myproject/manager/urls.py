from django.urls import path, re_path
from . import views

urlpatterns = [

    path('panel/manager/list/', views.manager_list, name='manager_list'),

    re_path(r'^panel/manager/del/(?P<pk>\d+)/$', views.manager_del, name='manager_del'),

 
    # groups
    path('panel/manager/group/', views.manager_group, name='manager_group'),

    path('panel/manager/group/add/', views.manager_group_add, name='manager_group_add'),

    re_path(r'^panel/manager/group/del/(?P<name>.*)/$', views.manager_group_del, name='manager_group_del'),

    re_path(r'^panel/manager/group/show/(?P<pk>\d+)/$', views.users_groups, name='users_groups'),

    re_path(r'^panel/manager/addtogroup/(?P<pk>\d+)/$', views.add_users_to_groups, name='add_users_to_groups'),

    re_path(r'^panel/manager/group/remove/(?P<pk>\d+)/(?P<name>.*)/$', views.del_users_from_groups, name='del_users_from_groups'),


    # permissions
    path('panel/manager/permission/', views.manager_permission, name='manager_permission'),
    
    re_path(r'^panel/manager/permission/del/(?P<name>.*)/$', views.manager_permission_del, name='manager_permission_del'),
    
    path('panel/manager/permission/add/', views.manager_permission_add, name='manager_permission_add'),
    
    re_path(r'^panel/manager/permission/show/(?P<pk>\d+)/$', views.users_permission, name='users_permission'),

    re_path(r'^panel/manager/permission/remove/(?P<pk>\d+)/(?P<name>.*)/$', views.users_permission_del, name='users_permission_del'),

    re_path(r'^panel/manager/permission/add/(?P<pk>\d+)/$', views.users_permission_add, name='users_permission_add'),


    # add permission to group
    re_path(r'^panel/manager/add/permission/group/(?P<name>.*)/$', views.groups_permissions, name='groups_permissions'),
    re_path(r'^panel/manager/del/permission/group/(?P<gname>.*)/(?P<name>.*)$', views.groups_permissions_del, name='groups_permissions_del'),
    re_path(r'^panel/manager/group/addperms/(?P<name>.*)/$', views.groups_permissions_add, name='groups_permissions_add'),



]