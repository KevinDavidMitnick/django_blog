from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name  = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.CharField(max_length=255)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    read_count = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail",kwargs={'pk':self.pk})

    def increase_readcnt(self):
        self.read_count += 1
        self.save(update_fields=['read_count'])

