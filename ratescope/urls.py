from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
]
