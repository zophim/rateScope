from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', auth_views.login, name='login'), 
    url(r'^logout/', auth_views.logout, name='logout'), 
    url(r'^$', views.index, name='index'),
]
