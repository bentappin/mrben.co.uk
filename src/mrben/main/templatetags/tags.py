import re

from django import template


register = template.Library()


@register.filter(name='twitterize')
def twitterize(token):
    return re.sub(r'\B(@(\w+))', r'<a href="https://twitter.com/\2">\1</a>', token)
twitterize.is_safe = True
