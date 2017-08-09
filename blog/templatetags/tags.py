from django import template
from django.db.models.aggregates import Count
from ..models import Article,Category,Tag

register = template.Library()

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)
