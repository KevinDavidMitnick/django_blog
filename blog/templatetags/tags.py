from django import template
from ..models import Article,Category

register = template.Library()

@register.simple_tag
def get_categories():
    return Category.objects.all()
