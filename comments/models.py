from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    url = models.URLField()
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    article =  models.ForeignKey('blog.Article')

    def __unicode__(self):
        return self.text[:20]
