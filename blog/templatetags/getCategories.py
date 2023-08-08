from django import template
from blog.models import CategoryModel

register = template.Library()

@register.simple_tag
def get_categories():
    categories = CategoryModel.objects.all()
    return categories
    