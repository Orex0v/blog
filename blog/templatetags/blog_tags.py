from django import template
from ..models import Category

register = template.Library()


def get_categories(context, order, count):
    """Получаем список категорий"""
    categories = Category.objects.filter(published=True)
    if count is not None:
        categories = categories[:count]
    return categories


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def category_list(context, order = '-name', count=None, template='base/blog/categories.html'):
    """Template tag вывода категорий"""
    categories = get_categories(context, order, count)
    return {'template': template, 'category_list': categories}


@register.simple_tag(takes_context=True)
def for_category_list(context, count=None, order='-name'):
    """Template tag для вывода категорий без шаблона"""
    return get_categories(context, order, count)
