from django.contrib import admin

# Register your models here.
from . models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','article','create_time']

admin.site.register(Comment,CommentAdmin)
