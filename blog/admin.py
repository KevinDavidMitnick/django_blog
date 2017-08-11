from django.contrib import admin

# Register your models here.
from . models import Article,Tag,Author,Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modify_time','author']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','email']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Category,CategoryAdmin)
