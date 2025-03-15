from django import template

register = template.Library()


@register.filter(name="class_name")
def class_name(object):
    return object.__class__.__name__
