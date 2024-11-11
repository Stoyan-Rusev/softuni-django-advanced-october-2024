from datetime import datetime

from django import template

register = template.Library()


@register.simple_tag(name='time')
def show_current_time(format_string='%Y/%h/%d - %H:%M:%S'):
    return datetime.now().strftime(format_string)
