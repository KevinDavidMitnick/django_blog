from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    article =  models.ForeignKey('blog.Article')
    author  =  models.ForeignKey('users.User')

    def __unicode__(self):
        return self.text[:20]
