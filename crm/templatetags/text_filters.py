from django import template
import textwrap

register = template.Library()

@register.filter
def wrap_text(value, width=50):
    if not value:
        return ""
    lines = textwrap.wrap(str(value), width=int(width))
    return "<br>".join(lines)
