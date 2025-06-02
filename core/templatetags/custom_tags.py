from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, [])

@register.filter
def index(sequence, position):
    try:
        return sequence[position]
    except:
        return None

@register.filter(name='add_class')
def add_class(field, css_class):
    try:
        return field.as_widget(attrs={"class": css_class})
    except AttributeError:
        return field 