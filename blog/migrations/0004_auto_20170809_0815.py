# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_read_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]