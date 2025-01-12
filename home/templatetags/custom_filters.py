from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_price(value):
    return f"{value:,}"


@register.filter
def days_since(value):
    delta = datetime.now().date() - value.date()
    days = delta.days
    if days == 0:
        return "امروز"
    elif days == 1:
        return "دیروز"
    else:
        return f"{days} روز پیش"
