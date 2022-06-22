from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    """
    Custom tags to allow indication of current page on base template.
    """
    import re
    if re.search(pattern, request.path):
        return 'active' if pattern == request.path else ''
    return ''