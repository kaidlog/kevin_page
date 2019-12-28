"""kevin_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from classes.views import hello_world, index, bio, work,contact,post_create_feedback, test,test2


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hellonuts/$', hello_world),
    url(r'^$' , index),
    url(r'^bio/$', bio),
    url(r'^work/$', work),
    url(r'^contact/$', contact),
    url(r'feedback/post$', post_create_feedback),
    url(r'^test/$', test),

]
