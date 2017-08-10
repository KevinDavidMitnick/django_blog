from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    name  = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Article(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.CharField(max_length=255)
    content = models.TextField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
