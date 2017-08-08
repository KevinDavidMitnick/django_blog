"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^comments/', include('comments.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from users import views

app_name = 'users'
urlpatterns = [
    url(r'^register/$',views.register,name='register')
]
