"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^(?P<cid>[0-9]*)/$', views.index,name="index"),
    url(r'^about/$', views.about,name="about"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail,name="detail"),
    url(r'^contact/$', views.contact,name="contact"),
]
