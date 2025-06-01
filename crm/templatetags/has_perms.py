from django import template
from django.apps import apps
from django.urls import reverse_lazy
register = template.Library()
from django.templatetags.static import static


import textwrap

@register.filter
def wrap_text(value, width=50):
    if not value:
        return ""
    lines = textwrap.wrap(str(value), width=int(width))
    return "<br>".join(lines)

@register.filter
def has_perms(user, app_name):
    app_config = apps.get_app_config(app_name)
    if hasattr(app_config, 'sub_verbose_name'):
      return user.groups.filter(name=app_config.verbose_name).exists() or user.groups.filter(name=app_config.sub_verbose_name).exists()
    else:
      return user.groups.filter(name=app_config.verbose_name).exists()
 
  
@register.filter()
def url_logout(request):  # pylint:disable=unused-argument
    return reverse_lazy('logout')
 

@register.filter()
def url_login(request):  # pylint:disable=unused-argument
    return reverse_lazy('login')


@register.filter()
def get_default_avatar_url(user):
    url = static('assets/img/team/default.png')
    return url
