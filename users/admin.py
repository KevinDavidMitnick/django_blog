# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','password','nickname']

admin.site.register(User,UserAdmin)
