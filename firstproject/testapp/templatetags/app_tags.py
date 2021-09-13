from django import template
import datetime
register=template.Library()
@register.simple_tag(name="get_date")
def get_date():
    now=datetime.datetime.now()
    return now
@register.simple_tag(name="dict")
def dict():
    dicts={"1":1,"2":2}
    return dicts
@register.filter()
def string(value):
    t=str(value).split()
    return t
