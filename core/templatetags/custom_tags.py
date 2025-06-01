from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def index(sequence, position):
    return sequence[position] if position < len(sequence) else None