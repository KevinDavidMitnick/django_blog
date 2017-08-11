from django import template
from ..models import Article,Category

register = template.Library()

@register.simple_tag
def get_recent_articles(num=8):
    return Article.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def get_categories():
    return Category.objects.all()
